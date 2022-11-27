class ClientInfo:
    client_id = ""
    client_secret = ""

    @staticmethod
    def refresh(client_id, client_secret):
        ClientInfo.client_id = client_id
        ClientInfo.client_secret = client_secret


session_client_info = ClientInfo()


def get_client_id():
    return ClientInfo.client_id


def get_client_secret():
    return ClientInfo.client_secret


def change_config(client_id, client_secret):
    ClientInfo.refresh(client_id, client_secret)
