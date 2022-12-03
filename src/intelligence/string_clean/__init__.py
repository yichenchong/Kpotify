from ...logger import warning
from ....lib.unidecode import unidecode


def string_clean(string):
    """
    Clean a string to be comparable with a search string.
    Converts non-ASCII characters to ASCII and removes all non-alphanumeric characters.
    :param string: string to clean
    :type string: str
    :return: cleaned string
    :rtype: str
    """
    if isinstance(string, str):
        return unidecode(string).lower()
    else:
        warning("string_clean: string is not a string", string.__class__)
        return string
