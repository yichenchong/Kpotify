from ..base_settings import base_url


class PlayerAPIURLs:
    """
    PlayerAPIURLs is a singleton class, which holds the urls for the player api.
    """
    get_currently_playing = base_url + '/me/player/currently-playing'
    get_devices = base_url + '/me/player/devices'
    get_playback = base_url + '/me/player'
    get_recently_played = base_url + '/me/player/recently-played'
    pause = base_url + '/me/player/pause'
    play = base_url + '/me/player/play'
    seek_to_position = base_url + '/me/player/seek'
    set_repeat = base_url + '/me/player/repeat'
    set_volume = base_url + '/me/player/volume'
    skip_next = base_url + '/me/player/next'
    skip_previous = base_url + '/me/player/previous'
    transfer_playback = base_url + '/me/player'
    toggle_shuffle = base_url + '/me/player/shuffle'
    add_to_queue = base_url + '/me/player/queue'
