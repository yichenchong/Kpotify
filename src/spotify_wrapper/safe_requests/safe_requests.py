import json

from ..auth.auth import AuthService
from ....lib import requests as requests


class SafeRequests:
    """
    Safe requests class.
    Makes requests, but guarantees that the access token is valid.
    """

    @staticmethod
    def __access_token__():
        """
        Get access token from auth service.
        :return: access token
        :rtype str
        """
        return "Bearer " + AuthService.get_access_token()

    @staticmethod
    def get(url, headers=None, params=None):
        """
        Make GET request.

        :param url: url to make request to
        :param headers: headers to send with request
        :type headers: dict
        :param params: params to send with request
        :type params: dict
        :return: response
        :rtype requests.Response
        """
        if headers is None:
            headers = {"Authorization": SafeRequests.__access_token__()}
        else:
            headers["Authorization"] = SafeRequests.__access_token__()
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 401:
            AuthService.refresh_access_token()
            headers["Authorization"] = SafeRequests.__access_token__()
            r = requests.get(url, headers=headers, params=params)
        return r

    @staticmethod
    def post(url, data=None, headers=None, params=None):
        """
        Make POST request.

        :param url: url to make request to
        :type url: str
        :param data: data to send with request
        :type data: dict
        :param headers: headers to send with request
        :type headers: dict
        :param params: params to send with request
        :type params: dict
        :return: response
        :rtype requests.Response
        """
        if headers is None:
            headers = {"Authorization": SafeRequests.__access_token__()}
        else:
            headers["Authorization"] = SafeRequests.__access_token__()
        if isinstance(data, dict):
            data = json.dumps(data)
        r = requests.post(url, data=data, headers=headers, params=params)
        if r.status_code == 401:
            AuthService.refresh_access_token()
            headers["Authorization"] = SafeRequests.__access_token__()
            r = requests.post(url, data=data, headers=headers, params=params)
        return r

    @staticmethod
    def put(url, data=None, headers=None, params=None):
        """
        Make PUT request.

        :param url: url to make request to
        :type url: str
        :param data: data to send with request
        :type data: dict
        :param headers: headers to send with request
        :type headers: dict
        :param params: params to send with request
        :type params: dict
        :return: response
        :rtype requests.Response
        """
        if headers is None:
            headers = {"Authorization": SafeRequests.__access_token__()}
        else:
            headers["Authorization"] = SafeRequests.__access_token__()
        if isinstance(data, dict):
            data = json.dumps(data)
        r = requests.put(url, data=data, headers=headers, params=params)
        if r.status_code == 401:
            AuthService.refresh_access_token()
            headers["Authorization"] = SafeRequests.__access_token__()
            r = requests.put(url, data=data, headers=headers, params=params)
        return r

    @staticmethod
    def delete(url, headers=None, params=None):
        """
        Make DELETE request.

        :param url: url to make request to
        :type url: str
        :param headers: headers to send with request
        :type headers: dict
        :param params: params to send with request
        :type params: dict
        :return: response
        :rtype requests.Response
        """
        if headers is None:
            headers = {"Authorization": SafeRequests.__access_token__()}
        else:
            headers["Authorization"] = SafeRequests.__access_token__()
        r = requests.delete(url, headers=headers, params=params)
        if r.status_code == 401:
            AuthService.refresh_access_token()
            headers["Authorization"] = SafeRequests.__access_token__()
            r = requests.delete(url, headers=headers, params=params)
        return r

    @staticmethod
    def patch(url, data=None, headers=None, params=None):
        """
        Make PATCH request.

        :param url: url to make request to
        :type url: str
        :param data: data to send with request
        :type data: dict
        :param headers: headers to send with request
        :type headers: dict
        :param params: params to send with request
        :type params: dict
        :return: response
        :rtype requests.Response
        """
        if headers is None:
            headers = {"Authorization": SafeRequests.__access_token__()}
        else:
            headers["Authorization"] = SafeRequests.__access_token__()
        if isinstance(data, dict):
            data = json.dumps(data)
        r = requests.patch(url, data=data, headers=headers, params=params)
        if r.status_code == 401:
            AuthService.refresh_access_token()
            headers["Authorization"] = SafeRequests.__access_token__()
            r = requests.patch(url, data=data, headers=headers, params=params)
        return r

