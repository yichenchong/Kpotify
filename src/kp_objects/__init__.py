from .items.categories import Registry as Registry
from .image_downloader import image_downloader_config as id_config


def on_config_change(config):
    """
    Callback for config changes.

    :param config: new config
    :type config: dict
    :return: None
    """
    id_config.change_config(config.get("load_icons"))
