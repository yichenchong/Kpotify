from .player.player import Player as Player
from .search.search import Search as Search

from .auth.auth_config_handler import change_config as change_auth_config
from .base_settings import reload_config as reload_base_config


def on_config_change(config):
    """
    Callback for config changes.

    :param config: new config
    :type config: dict
    :return: None
    """
    change_auth_config(config["client_id"], config["client_secret"])
    reload_base_config(config["device_id"])
