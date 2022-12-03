from . import Track
from . import Album
from . import Artist
from . import Playlist
from ...logger import warning


class Registry:
    user_base = 0
    categories = [
        Track,
        Album,
        Artist,
        Playlist
    ]

    @staticmethod
    def register_categories(user_base):
        Registry.user_base = user_base
        actions_tree = {}
        for i in range(len(Registry.categories)):
            Registry.categories[i].category = Registry.user_base + i + 1
            for j in Registry.categories[i].actions():
                actions_tree[Registry.categories[i].category] = [
                    action.to_kp_action_dict()
                    for action in Registry.categories[i].actions()
                ]
        return actions_tree

    @staticmethod
    def execute(item, action):
        item_category = item.category()
        if (item_category - Registry.user_base - 1 >= len(Registry.categories)
                or item_category - Registry.user_base - 1 < 0):
            warning("Item category not found in Registry")
            return
        Registry.categories[item_category - Registry.user_base - 1].execute(item, action)


