import hashlib
import string

from .auth_config_handler import get_client_id, get_client_secret
from .auth_data import AuthData
from .auth_server import wait_for_auth_code
import base64
import random
from ....lib import requests as requests
import urllib.parse
import webbrowser

scope = "user-read-playback-state user-modify-playback-state"
MAX_RETRIES = 100


class AuthService:
    """
    Handles authentication with Spotify.

    This class is responsible for getting an access token from Spotify.
    """
    @staticmethod
    def basic_auth():
        """
        Get the basic authorization header.
        :return:
        """
        return "Basic " + base64.b64encode(
            (get_client_id() + ":" + get_client_secret()).encode()
        ).decode()

    @staticmethod
    def get_new_tokens():
        """
        Get new access and refresh tokens from Spotify from scratch.
        """
        # make a new request for tokens
        local_state = str(random.randint(0, 100000))
        code_verifier = ''.join([random.choice(string.ascii_letters) for _ in range(128)])
        code_challenge = base64.urlsafe_b64encode(
            hashlib.sha256(code_verifier.encode()).digest()
        ).decode().replace('=', '')
        login_params = {
            'response_type': 'code',
            'client_id': get_client_id(),
            'scope': scope,
            'redirect_uri': 'http://localhost:8000',
            'state': local_state,
            'code_challenge_method': 'S256',
            'code_challenge': code_challenge
        }
        webbrowser.open('https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(login_params))
        code, state = wait_for_auth_code()
        print(code, state)
        if state != local_state:
            print("State mismatch")
            # TODO: log error
            return None
        token_params = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://localhost:8000',
            'code_verifier': code_verifier
        }
        headers = {
            "Authorization": AuthService.basic_auth(),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post(
            'https://accounts.spotify.com/api/token',
            data=token_params,
            headers=headers
        )
        if r.status_code == 200:
            json = r.json()
            AuthData.set_refresh_token(json['refresh_token'])
            AuthData.set_access_token(json['access_token'])
            return AuthData.get_access_token()
        else:
            print("Error getting access token")
            print(r.content)
            # TODO: log error
            return None

    @staticmethod
    def get_access_token():
        """
        Get the access token from AuthData.
        If the access token is invalid, refresh it.

        :return: The access token.
        :rtype: str
        """
        auth_data_token = AuthData.get_access_token()
        if auth_data_token is not None:
            return auth_data_token
        counter = 0
        while auth_data_token is None:
            if counter >= MAX_RETRIES:
                break
            AuthService.refresh_access_token()
            auth_data_token = AuthData.get_access_token()
            counter += 1
        return auth_data_token


    @staticmethod
    def refresh_access_token():
        """
        Refresh the access token.
        """

        # get refresh token from AuthData
        refresh_token = AuthData.get_refresh_token()

        token_params = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'redirect_uri': 'http://localhost:8000',
            'client_id': get_client_id()
        }
        headers = {
            "Authorization": AuthService.basic_auth()
        }
        r = requests.post(
            'https://accounts.spotify.com/api/token',
            data=token_params,
            headers=headers
        )
        print("Refreshing access token")
        try:
            AuthData.set_access_token(r.json()['access_token'])
            if "refresh_token" in r.json():
                AuthData.set_refresh_token(r.json()['refresh_token'])
        except KeyError:
            AuthData.clear_tokens()
            AuthService.get_new_tokens()