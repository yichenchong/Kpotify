from ...image_downloader import ImageDownloader
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

    def __init__(self, name, genres, uri, images=None):
        self.name = name
        self.genres = genres
        self.uri = uri
        self.image_url = images[-1]["url"] if images is not None and len(images) > 0 else None

    def label(self):
        return self.name

    def description(self):
        return f"Artist: {', '.join(self.genres)}"

    def target(self):
        return self.uri

    def icon_handle(self):
        return ImageDownloader().download(self.image_url)

    def data_bag(self):
        return ""
