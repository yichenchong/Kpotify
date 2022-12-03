from ...image_downloader import ImageDownloader
from ....spotify_wrapper import Player
from ..item import Item
from .actions import PlayAlbum


class Album(Item):
    @staticmethod
    def execute(item, action):
        if action is None or action.name() == PlayAlbum().name():
            Player.play(
                context_uri=item.target().strip("\"")
            )

    @staticmethod
    def actions():
        return [
            PlayAlbum()
        ]

    def __init__(self, name, artists, uri, release_date=None, images=None):
        self.name = name
        self.release_date = release_date
        self.image_url = images[-1]["url"] if images is not None and len(images) > 0 else None
        self.artists = artists
        self.uri = uri

    def label(self):
        return self.name

    def description(self):
        return f"Album: {', '.join(self.artists)} ({self.release_date})"

    def target(self):
        return self.uri

    def icon_handle(self):
        return ImageDownloader().download(self.image_url)

    def data_bag(self):
        return ""
