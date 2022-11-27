from ..action import Action


class PlayArtist(Action):
    def name(self):
        return 'play_artist'

    def label(self):
        return 'Play'

    def short_desc(self):
        return 'Play this artist'

    def data_bag(self):
        return ""
