import os


class AuthData:
    """
    This class is used to store and retrieve the refresh and access tokens.
    """
    access_token = None
    # this file's directory
    dir = os.path.dirname(__file__)
    refresh_token_path = os.path.join(dir, 'refresh_token')
    refresh_token = None

    @staticmethod
    def set_refresh_token(refresh_token):
        """
        Store refresh token in file.

        :param refresh_token: The refresh token to store.
        :ptype refresh_token: str
        """
        # store refresh token in a file
        AuthData.refresh_token = refresh_token
        with open(AuthData.refresh_token_path, 'w') as f:
            f.write(refresh_token)

    @staticmethod
    def set_access_token(access_token):
        """
        Store access token in static variable.

        :param access_token: The access token to store.
        :ptype access_token: str
        """
        AuthData.access_token = access_token

    @staticmethod
    def get_refresh_token():
        """
        Get refresh token locally or from file.

        :return: refresh token
        :rtype: str
        """
        if AuthData.refresh_token is not None:
            return AuthData.refresh_token
        try:
            with open(AuthData.refresh_token_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None


    @staticmethod
    def get_access_token():
        """
        Get access token from static variable.

        :return: access token
        :rtype: str
        """
        # get access token from static variable
        return AuthData.access_token

    @staticmethod
    def clear_tokens():
        """Clear the refresh token and access token."""
        AuthData.access_token = None
        with open(AuthData.refresh_token_path, 'w') as f:
            f.write("")
