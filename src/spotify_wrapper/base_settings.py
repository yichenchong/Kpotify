base_url = 'https://api.spotify.com/v1'


class BaseSettings:
    """
    BaseSettings is a singleton class, which holds the base settings for the spotify wrapper.
    """
    def __init__(self):
        self.device_id = ''

    def get_device_id(self):
        """
        Get device id from cached BaseSettings instance.

        :return device id
        :rtype  str
        """
        return self.device_id


settings = BaseSettings()


def reload_config(new_id=None):
    """
    reload config from config file.

    :param new_id: new device id
    :ptype new_id: str
    """
    if new_id is not None:
        settings.device_id = new_id
