from ..action import Action


class PlayAlbum(Action):
    def name(self):
        return 'play_album'

    def label(self):
        return 'Play'

    def short_desc(self):
        return 'Play this album'

    def data_bag(self):
        return ""
