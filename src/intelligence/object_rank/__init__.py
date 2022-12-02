from .item_scores import score_item


def rank(suggestions, query, mod=1):
    """
    Rerank a list of suggestions based on the query.
    :param suggestions: list of suggestions
    :type suggestions: list[.kp_objects.items.Item]
    :param query: query to rerank suggestions with
    :type query: str
    :return: ranked suggestions
    :rtype: list[.kp_objects.items.Item]
    """
    def current_location(item):
        return suggestions.index(item)
    return sorted(suggestions, key=lambda item: score_item(item, query, -(current_location(item) % mod)), reverse=True)