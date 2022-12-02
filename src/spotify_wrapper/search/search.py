from enum import Enum

from .search_api_urls import SearchAPIUrls as urls
from ..safe_requests.safe_requests import SafeRequests as Requests


class Search:
    """
    A class that offers methods to search for tracks, albums, artists, playlists, and shows.
    """
    @staticmethod
    def search(query, types, market=None, limit=None, offset=None):
        """
        Search for an item.

        :param query: query to search for
        :type query: str
        :param types: types of items to search for
        :type types: list
        :param market: filter results by market
        :type market: str
        :param limit: limit the number of items returned
        :type limit: int
        :param offset: offset the number of items returned
        :type offset: int
        :return: response
        :rtype requests.Response
        """
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
        """
        An enum that represents the types of items to search for.
        """
        ALBUM = "album"
        ARTIST = "artist"
        PLAYLIST = "playlist"
        TRACK = "track"
        SHOW = "show"
        EPISODE = "episode"
        AUDIOBOOK = "audiobook"
