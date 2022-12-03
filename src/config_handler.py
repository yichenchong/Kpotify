from .spotify_wrapper import on_config_change as spotify_wrapper_on_config_change
from .kp_objects import on_config_change as kp_objects_on_config_change


def on_config_change(config):
    """
    Callback for config changes.

    :param config: new config
    :type config: dict
    :return: None
    """
    spotify_wrapper_on_config_change(config)
    kp_objects_on_config_change(config)
