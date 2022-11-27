from ....spotify_wrapper import Player
from ..item import Item
from .actions import PlayArtist


class Artist(Item):
    @staticmethod
    def execute(item, action):
        if action is None or action.name() == PlayArtist().name():
            Player.play(
                context_uri=item.target().strip("\"")
            )

    @staticmethod
    def actions():
        return [
            PlayArtist()
        ]

    def __init__(self, name, genres, uri, image_url=None):
        self.name = name
        self.genres = genres
        self.image_url = image_url
        self.uri = uri

    def label(self):
        return self.name

    def description(self):
        return f"{', '.join(self.genres)}"

    def target(self):
        return self.uri

    def icon_handle(self):
        return None

    def data_bag(self):
        return ""
