from .. import spotify_wrapper as wrapper
from ..kp_objects import items as items


class KpotParse:
    @staticmethod
    def parse(user_input):
        user_input = user_input.lower()
        if not user_input.startswith("kpot "):
            return None
        suggestions = []
        user_input = user_input[5:]
        suggestions.extend(KpotPlayer.parse(user_input))
        suggestions.extend(KpotSearch.parse(user_input))
        return suggestions


class KpotPlayer:
    # TODO: parse player control commands
    @staticmethod
    def parse(user_input):
        return []


class KpotSearch:
    @staticmethod
    def parse(user_input):
        if user_input.startswith("search "):
            user_input = user_input[7:]
        if user_input.startswith("play "):
            user_input = user_input[5:]
        if user_input.startswith("artist "):
            user_input = user_input[7:]
            search_types = [wrapper.Search.SearchType.ARTIST]
        elif user_input.startswith("album "):
            user_input = user_input[6:]
            search_types = [wrapper.Search.SearchType.ALBUM]
        elif user_input.startswith("track "):
            user_input = user_input[6:]
            search_types = [wrapper.Search.SearchType.TRACK]
        elif user_input.startswith("playlist "):
            user_input = user_input[9:]
            search_types = [wrapper.Search.SearchType.PLAYLIST]
        elif user_input.startswith("something "):
            user_input = user_input[10:]
            search_types = KpotSearch.parse_something(user_input)
            pass  # TODO: parse something by relevance
            return []
        else:
            search_types = KpotSearch.parse_all(user_input)
            return []
            # TODO: parse all by relevance
        # TODO: add search type "my playlists"
        resp = wrapper.Search.search(user_input, search_types)
        if resp.status_code != 200:
            return []
        search = resp.json()
        tracks = search.get("tracks", {}).get("items", [])
        albums = search.get("albums", {}).get("items", [])
        artists = search.get("artists", {}).get("items", [])
        playlists = search.get("playlists", {}).get("items", [])
        suggestions = []
        suggestions.extend([
            items.Track(
                track["name"],
                track["album"]["name"],
                [artist["name"] for artist in track["artists"]],
                track["uri"],
                track["duration_ms"]
            ) for track in tracks
        ])
        suggestions.extend([
            items.Album(
                album["name"],
                [artist["name"] for artist in album["artists"]],
                album["uri"],
                release_date=album["release_date"],
                image_url=album["images"][0]["url"] if album["images"] else None
            ) for album in albums
        ])
        suggestions.extend([
            items.Artist(
                artist["name"],
                artist["genres"],
                artist["uri"],
                image_url=artist["images"][0]["url"] if artist["images"] else None
            ) for artist in artists
        ])
        suggestions.extend([
            items.Playlist(
                playlist["name"],
                playlist["owner"]["display_name"],
                playlist["description"],
                playlist["uri"],
                image_url=playlist["images"][0]["url"] if playlist["images"] else None
            ) for playlist in playlists
        ])

        return suggestions
        # TODO: parse play search query

    @staticmethod
    def parse_artist():
        return [wrapper.Search.SearchType.ARTIST]

    @staticmethod
    def parse_album():
        return [wrapper.Search.SearchType.ALBUM]

    @staticmethod
    def parse_track():
        return [wrapper.Search.SearchType.TRACK]

    @staticmethod
    def parse_playlist():
        return [wrapper.Search.SearchType.PLAYLIST]

    @staticmethod
    def parse_all(user_input):
        return [
            wrapper.Search.SearchType.ALBUM,
            wrapper.Search.SearchType.TRACK,
            wrapper.Search.SearchType.PLAYLIST
        ]

    @staticmethod
    def parse_something(user_input):
        return [
            wrapper.Search.SearchType.ALBUM,
            wrapper.Search.SearchType.TRACK,
            wrapper.Search.SearchType.PLAYLIST
        ]