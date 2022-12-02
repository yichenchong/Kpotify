import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import sleep, time

from .. import spotify_wrapper as wrapper
from ..kp_objects import items as items
from ..intelligence import object_rank as ranker

executor = ThreadPoolExecutor(max_workers=4)

class SearchCounter:
    """
    A class to keep track of the number of searches.
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get(self):
        return self.count


sc = SearchCounter()


class KpotParse:

    @staticmethod
    def parse(user_input):
        user_input = user_input.lower()
        if not user_input.startswith("kpot "):
            return None
        suggestions = []
        user_input = user_input[5:]
        parser_futures = [
            executor.submit(KpotPlayer.parse, user_input),
            executor.submit(KpotSearch.parse, user_input)
        ]
        for future in parser_futures:
            suggestions.extend(future.result())
        return suggestions


class KpotPlayer:
    # TODO: parse player control commands
    @staticmethod
    def parse(user_input):
        return []


class KpotSearch:
    @staticmethod
    def parse(user_input):
        # eliminate searching while typing
        sc.increment()
        cur = sc.get()
        t = time()
        while time() - t < 0.3:
            sleep(0.05)
            if sc.get() > cur:
                return []
        # start parsing searches
        if user_input.startswith("search "):
            user_input = user_input[7:]
        if user_input.startswith("play "):
            user_input = user_input[5:]
        # searching parsing
        if user_input.startswith("artist "):
            return KpotSearch.parse_artist(user_input[7:])
        elif user_input.startswith("album "):
            return KpotSearch.parse_album(user_input[6:])
        elif user_input.startswith("track "):
            return KpotSearch.parse_track(user_input[6:])
        elif user_input.startswith("playlist "):
            return KpotSearch.parse_playlist(user_input[9:])
        elif user_input.startswith("something "):
            user_input = user_input[10:]
            # search_types = KpotSearch.parse_something(user_input)
            pass  # TODO: parse something by relevance
            return []
        else:
            return KpotSearch.parse_all(user_input)

    @staticmethod
    def parse_artist(user_input, limit=20):
        resp = wrapper.Search.search(user_input, [wrapper.Search.SearchType.ARTIST])
        if resp.status_code != 200:
            return []
        search = resp.json()
        artists = search.get("artists", {}).get("items", [])
        suggestions = [items.Artist(artist["name"], artist["genres"], artist["uri"]) for artist in artists]
        return suggestions

    @staticmethod
    def parse_album(user_input, limit=20):
        resp = wrapper.Search.search(user_input, [wrapper.Search.SearchType.ALBUM])
        if resp.status_code != 200:
            return []
        search = resp.json()
        albums = search.get("albums", {}).get("items", [])
        suggestions = [
            items.Album(
                album["name"],
                [artist["name"] for artist in album["artists"]],
                album["name"]
            ) for album in albums
        ]
        return suggestions

    @staticmethod
    def parse_track(user_input, limit=20):
        resp = wrapper.Search.search(user_input, [wrapper.Search.SearchType.TRACK])
        if resp.status_code != 200:
            return []
        search = resp.json()
        tracks = search.get("tracks", {}).get("items", [])
        suggestions = [
            items.Track(
                track["name"],
                track["album"]["name"],
                [artist["name"] for artist in track["artists"]],
                track["uri"],
                track["duration_ms"]
            ) for track in tracks
        ]
        return suggestions

    @staticmethod
    def parse_playlist(user_input, limit=20):
        resp = wrapper.Search.search(user_input, [wrapper.Search.SearchType.PLAYLIST])
        if resp.status_code != 200:
            return []
        search = resp.json()
        playlists = search.get("playlists", {}).get("items", [])
        suggestions = [
            items.Playlist(
                playlist["name"],
                playlist["owner"]["display_name"],
                playlist["description"],
                playlist["uri"]
            ) for playlist in playlists
        ]
        return suggestions

    @staticmethod
    def parse_all(user_input):
        search_futures = [
            executor.submit(KpotSearch.parse_artist, user_input),
            executor.submit(KpotSearch.parse_album, user_input),
            executor.submit(KpotSearch.parse_track, user_input),
            executor.submit(KpotSearch.parse_playlist, user_input)
        ]
        suggestions = []
        for future in search_futures:
            suggestions.extend(future.result())
        return ranker.rank(suggestions, user_input, 5)

    @staticmethod
    def parse_something():
        return [
            wrapper.Search.SearchType.ALBUM,
            wrapper.Search.SearchType.TRACK,
            wrapper.Search.SearchType.PLAYLIST
        ]