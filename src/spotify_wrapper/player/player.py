from .player_api_urls import PlayerAPIURLs as urls
from ..base_settings import device_id
from ..safe_requests.safe_requests import SafeRequests as Requests


class Player:
    @staticmethod
    def __try_device_id__(method, url, *args, **kwargs):
        r = method(url, *args, **kwargs)
        if r.status_code == 404:
            if 'device' in r.json()['error']['message']:
                params = kwargs.get('params', {})
                params['device_id'] = device_id
                kwargs['params'] = params
                r = method(url, *args, **kwargs)
        return r

    @staticmethod
    def get_currently_playing():
        return Requests.get(urls.get_currently_playing)

    @staticmethod
    def get_devices():
        return Requests.get(urls.get_devices)

    @staticmethod
    def get_playback():
        return Requests.get(urls.get_playback)

    @staticmethod
    def get_recently_played(after, before, limit):
        params = {
            "after": after,
            "before": before,
            "limit": limit
        }
        return Requests.get(urls.get_recently_played, params=params)

    @staticmethod
    def pause():
        return Player.__try_device_id__(Requests.put, urls.pause)

    @staticmethod
    def play(uris=None, context_uri=None, offset=None, position_ms=None):
        data = {
            "uris": uris,
            "context_uri": context_uri,
            "offset": offset,
            "position_ms": position_ms
        }
        return Player.__try_device_id__(Requests.put, urls.play, data=data)

    @staticmethod
    def seek_to_position(position_ms):
        return Player.__try_device_id__(Requests.put, urls.seek_to_position, params={'position_ms': position_ms})

    @staticmethod
    def set_repeat(state):
        return Player.__try_device_id__(Requests.put, urls.set_repeat, params={'state': state})

    @staticmethod
    def set_volume(volume_percent):
        return Player.__try_device_id__(Requests.put, urls.set_volume, params={'volume_percent': volume_percent})

    @staticmethod
    def skip_next():
        return Player.__try_device_id__(Requests.post, urls.skip_next)

    @staticmethod
    def skip_previous():
        return Player.__try_device_id__(Requests.post, urls.skip_previous)

    @staticmethod
    def transfer_playback(device_ids, play=False):
        return Requests.put(urls.transfer_playback, data={"device_ids": device_ids, "play": play})

    @staticmethod
    def toggle_shuffle(state):
        return Player.__try_device_id__(Requests.put, urls.toggle_shuffle, params={'state': state})

    @staticmethod
    def add_to_queue(uri):
        return Player.__try_device_id__(Requests.post, urls.add_to_queue, params={'uri': uri})