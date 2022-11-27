from .player.player import Player as Player
from .search.search import Search as Search

from .auth.auth_config_handler import change_config as change_auth_config


def on_config_change(config):
    change_auth_config(config["client_id"], config["client_secret"])
