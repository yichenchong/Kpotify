from ...image_downloader import ImageDownloader
from ....spotify_wrapper import Player
from ..item import Item
from .actions import PlayPlaylist


class Playlist(Item):
    @staticmethod
    def execute(item, action):
        if action is None or action.name() == PlayPlaylist().name():
            Player.play(
                context_uri=item.target().strip("\"")
            )

    @staticmethod
    def actions():
        return [
            PlayPlaylist()
        ]

    def __init__(self, name, owner, description, uri, images=None):
        self.name = name
        self.owner = owner
        self.desc = description
        self.image_url = images[-1]["url"] if images is not None and len(images) > 0 else None
        self.uri = uri

    def label(self):
        return self.name

    def description(self):
        return f"Playlist: {self.owner} - {self.desc}"

    def target(self):
        return self.uri

    def icon_handle(self):
        return ImageDownloader().download(self.image_url)

    def data_bag(self):
        return ""
