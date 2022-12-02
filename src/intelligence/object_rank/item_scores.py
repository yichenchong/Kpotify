from ...kp_objects.items import Track, Artist, Album, Playlist
from ..string_clean import string_clean


def score_item(item, query, base_score=0):
    """
    Score an item based on the query.
    :param item: item to score
    :type item: ..kp_objects.items.Item
    :param query: query to score item with
    :type query: str
    :param base_score: base score to add to the item's score
    :type base_score: float
    :return: score
    :rtype: float
    """
    query = string_clean(query)
    if isinstance(item, Track):
        return base_score + score_track(item, query)
    elif isinstance(item, Artist):
        return base_score + score_artist(item, query)
    elif isinstance(item, Album):
        return base_score + score_album(item, query)
    elif isinstance(item, Playlist):
        return base_score + score_playlist(item, query)
    else:
        return 0


def score_track(track, query):
    """
    Score a track based on the query.
    :param track: track to score
    :type track: ..kp_objects.items.Track
    :param query: query to score track with
    :type query: str
    :return: score
    :rtype: float
    """
    score = 0
    if query == string_clean(track.name):
        score += 5
    if query in string_clean(track.name):
        score += 2
    if query in string_clean(track.album):
        score += 0.25
    for artist in track.artists:
        if query in string_clean(artist):
            score += 0.1
    return score


def score_artist(artist, query):
    """
    Score an artist based on the query.
    :param artist: artist to score
    :type artist: ..kp_objects.items.Artist
    :param query: query to score artist with
    :type query: str
    :return: score
    :rtype: float
    """
    score = 0
    if query == string_clean(artist.name):
        score += 3
    if query in artist.name:
        score += 1.5
    for genre in artist.genres:
        if query in genre:
            score += 0.1
    return score


def score_album(album, query):
    """
    Score an album based on the query.
    :param album: album to score
    :type album: ..kp_objects.items.Album
    :param query: query to score album with
    :type query: str
    :return: score
    :rtype: float
    """
    score = 0
    if query == string_clean(album.name):
        score += 2
    if query in string_clean(album.name):
        score += 1
    for artist in album.artists:
        if query in string_clean(artist):
            score += 0.1
    return score


def score_playlist(playlist, query):
    """
    Score a playlist based on the query.
    :param playlist: playlist to score
    :type playlist: ..kp_objects.items.Playlist
    :param query: query to score playlist with
    :type query: str
    :return: score
    :rtype: float
    """
    score = 0
    if query == string_clean(playlist.name):
        score += 2
    if query in string_clean(playlist.name):
        score += 1
    if query in string_clean(playlist.owner):
        score += 0.1
    if query in string_clean(playlist.desc):
        score += 0.1
    return score
