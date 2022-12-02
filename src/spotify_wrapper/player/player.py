from .player_api_urls import PlayerAPIURLs as urls
from ..base_settings import settings
from ..safe_requests.safe_requests import SafeRequests as Requests


class Player:
    @staticmethod
    def __try_device_id__(method, url, *args, **kwargs):
        """
        Make request, if no active device is found, try to get config device id.

        :param method: method to call
        :type method: function
        :param url: url to make request to
        :type url: str
        :param args: args to pass to method
        :type args: list
        :param kwargs: kwargs to pass to method
        :type kwargs: dict
        :return: response
        :rtype requests.Response
        """
        r = method(url, *args, **kwargs)
        if r.status_code == 404:
            if 'device' in r.json()['error']['message']:
                params = kwargs.get('params', {})
                params['device_id'] = settings.get_device_id()
                kwargs['params'] = params
                r = method(url, *args, **kwargs)
        return r

    @staticmethod
    def get_currently_playing():
        """
        Get information about the user's current playback state, including track, track progress, and active device.

        :return: response
        :rtype requests.Response
        """
        return Requests.get(urls.get_currently_playing)

    @staticmethod
    def get_devices():
        """
        Get information about a user's available devices.

        :return: response
        :rtype requests.Response
        """
        return Requests.get(urls.get_devices)

    @staticmethod
    def get_playback():
        """
        Get information about playback state.

        :return: response
        :rtype requests.Response
        """
        return Requests.get(urls.get_playback)

    @staticmethod
    def get_recently_played(after, before, limit):
        """
        Get tracks from the current user's recently played tracks.

        :param after: A Unix timestamp in milliseconds.
                      Returns all items after (but not including) this cursor position.
        :type after: int
        :param before: A Unix timestamp in milliseconds.
                       Returns all items before (but not including) this cursor position.
        :type before: int
        :param limit: Number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        :type limit: int
        :return: response
        :rtype requests.Response
        """
        params = {
            "after": after,
            "before": before,
            "limit": limit
        }
        return Requests.get(urls.get_recently_played, params=params)

    @staticmethod
    def pause():
        """
        Pause playback on the user's account.
        If no active device is found, try to get config device id.

        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.put, urls.pause)

    @staticmethod
    def play(uris=None, context_uri=None, offset=None, position_ms=None):
        """
        Start/Resume playback on the user's account.
        If no active device is found, try to get config device id.

        :param uris: uris of tracks to play
        :type uris: list
        :param context_uri: uri of context to play
        :type context_uri: str
        :param offset: uri of track to start at
        :type offset: str
        :param position_ms: position in ms to start at
        :type position_ms: int
        :return: response
        :rtype requests.Response
        """
        data = {
            "uris": uris,
            "context_uri": context_uri,
            "offset": offset,
            "position_ms": position_ms
        }
        return Player.__try_device_id__(Requests.put, urls.play, data=data)

    @staticmethod
    def seek_to_position(position_ms):
        """
        Seeks to the given position in the user's currently playing track.
        If no active device is found, try to get config device id.

        :param position_ms: position in ms to seek to
        :type position_ms: int
        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.put, urls.seek_to_position, params={'position_ms': position_ms})

    @staticmethod
    def set_repeat(state):
        """
        Set the repeat mode for the user's playback.
        Options are repeat-track, repeat-context, and off.
        If no active device is found, try to get config device id.

        :param state: desired state
        :type state: str
        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.put, urls.set_repeat, params={'state': state})

    @staticmethod
    def set_volume(volume_percent):
        """
        Set the volume for the user's current playback device.
        If no active device is found, try to get config device id.

        :param volume_percent: volume in percent from 0 to 100
        :type volume_percent: int
        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.put, urls.set_volume, params={'volume_percent': volume_percent})

    @staticmethod
    def skip_next():
        """
        Skips to next track in the user's queue.
        If no active device is found, try to get config device id.

        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.post, urls.skip_next)

    @staticmethod
    def skip_previous():
        """
        Skips to previous track in the user's queue.
        If no active device is found, try to get config device id.

        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.post, urls.skip_previous)

    @staticmethod
    def transfer_playback(device_ids, play=False):
        """
        Transfer playback to a new device and determine if it should start playing.

        :param device_ids: device ids to transfer to
        :type device_ids: list
        :param play: whether to play on transfer
        :type play: bool
        :return: response
        :rtype requests.Response
        """
        return Requests.put(urls.transfer_playback, data={"device_ids": device_ids, "play": play})

    @staticmethod
    def toggle_shuffle(state):
        """
        Toggle shuffle on or off for user's playback.
        If no active device is found, try to get config device id.

        :param state: desired state
        :type state: bool
        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.put, urls.toggle_shuffle, params={'state': state})

    @staticmethod
    def add_to_queue(uri):
        """
        Add an item to the end of the user's current playback queue.
        If no active device is found, try to get config device id.

        :param uri: uri of item to add
        :type uri: str
        :return: response
        :rtype requests.Response
        """
        return Player.__try_device_id__(Requests.post, urls.add_to_queue, params={'uri': uri})