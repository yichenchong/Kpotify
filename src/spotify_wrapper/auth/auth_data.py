import os


class AuthData:
    access_token = None
    # this file's directory
    dir = os.path.dirname(__file__)
    refresh_token_path = os.path.join(dir, 'refresh_token')

    @staticmethod
    def set_refresh_token(refresh_token):
        # store refresh token in a file
        with open(AuthData.refresh_token_path, 'w') as f:
            f.write(refresh_token)

    @staticmethod
    def set_access_token(access_token):
        # store access token in static variable
        AuthData.access_token = access_token
        print(f"Access token set to {access_token}")

    @staticmethod
    def get_refresh_token():
        # get refresh token from file
        try:
            with open(AuthData.refresh_token_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None


    @staticmethod
    def get_access_token():
        # get access token from static variable
        return AuthData.access_token

    @staticmethod
    def clear_tokens():
        AuthData.access_token = None
        with open(AuthData.refresh_token_path, 'w') as f:
            f.write("")
