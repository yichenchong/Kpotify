from ..item import Item
from .actions import PlayTrack, AddToQueue
from ...image_downloader import ImageDownloader
from ....spotify_wrapper import Player, Search


class Track(Item):
    @staticmethod
    def execute(item, action):
        if action is None or action.name() == PlayTrack().name():
            Player.play(
                uris=[item.target().strip("\"")]
            )
        elif action.name() == AddToQueue().name():
            Player.add_to_queue(item.target().strip("\""))

    @staticmethod
    def actions():
        return [
            PlayTrack(),
            AddToQueue()
        ]

    def __init__(self, name, album, artists, uri, duration_ms=None, images=None):
        self.name = name
        self.album = album
        self.artists = artists
        self.uri = uri
        self.duration_ms = duration_ms
        self.image_url = images[-1]["url"] if images is not None and len(images) > 0 else None

    def label(self):
        return self.name

    def description(self):
        if self.duration_ms is None:
            return f"Track: {', '.join(self.artists)} - {self.album}"
        return f"Track: {', '.join(self.artists)} - {self.album} ({self.duration_ms / 1000}s)"

    def target(self):
        return self.uri

    def icon_handle(self):
        return ImageDownloader().download(self.image_url)

    def data_bag(self):
        return ""
