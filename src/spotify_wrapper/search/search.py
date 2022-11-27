from enum import Enum

from .search_api_urls import SearchAPIUrls as urls
from ..safe_requests.safe_requests import SafeRequests as Requests

class Search:
    @staticmethod
    def search(query, types, market=None, limit=None, offset=None):
        params = {
            "q": query,
            "type": [type.value if isinstance(type, Enum) else type for type in types],
            "market": market,
            "limit": limit,
            "offset": offset
        }
        r = Requests.get(urls.search, params=params)
        return r

    class SearchType(Enum):
        ALBUM = "album"
        ARTIST = "artist"
        PLAYLIST = "playlist"
        TRACK = "track"
        SHOW = "show"
        EPISODE = "episode"
        AUDIOBOOK = "audiobook"
