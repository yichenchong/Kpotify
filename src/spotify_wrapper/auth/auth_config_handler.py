"""
Spotify application client ID and client secret configuration handler.
"""


class ClientInfo:
    """Class to hold client information for Spotify API authentication."""
    client_id = ""
    client_secret = ""

    @staticmethod
    def refresh(client_id, client_secret):
        """Refresh the client information."""
        ClientInfo.client_id = client_id
        ClientInfo.client_secret = client_secret


session_client_info = ClientInfo()


def get_client_id():
    """
    Get the client ID.

    :return: client ID
    :rtype: str
    """
    return ClientInfo.client_id


def get_client_secret():
    """
    Get the client secret.

    :return: client secret
    :rtype: str
    """
    return ClientInfo.client_secret


def change_config(client_id, client_secret):
    """
    Change the client ID and client secret.

    :param client_id: new client ID
    :ptype client_id: str
    :param client_secret: new client secret
    :ptype client_secret: str
    """
    ClientInfo.refresh(client_id, client_secret)
