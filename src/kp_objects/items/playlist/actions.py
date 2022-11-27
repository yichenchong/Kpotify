from ..action import Action


class PlayPlaylist(Action):
    def name(self):
        return 'play_playlist'

    def label(self):
        return 'Play'

    def short_desc(self):
        return 'Play this playlist'

    def data_bag(self):
        return ""
