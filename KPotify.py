from .src.kp_objects import Registry
from .src.spotify_wrapper import on_config_change
from .src.parsing_client import parse as Parse
import keypirinha as kp


class KPotify(kp.Plugin):
    """
    A KeyPirinha plugin to control Spotify
    """
    configs = [
        ("client_id", "spotify"),
        ("client_secret", "spotify")
    ]

    def on_start(self):
        action_tree = Registry.register_categories(kp.ItemCategory.USER_BASE)
        for category in action_tree:
            actions = [
                self.create_action(**action)
                for action in action_tree[category]
            ]
            self.set_actions(category, actions)
        settings = self.load_settings()
        on_config_change({
            setting[0]: settings.get_stripped(setting[0], setting[1])
            for setting in self.configs
        })

    def on_catalog(self):
        return

    def on_suggest(self, user_input, items_chain):
        if not user_input.startswith("kpot"):
            return
        suggested_items = Parse.parse(user_input)
        if suggested_items is None or suggested_items == []:
            return
        self.set_suggestions([
            self.create_item(**item.to_kp_item_dict())
            for item in suggested_items
        ], kp.Match.ANY, kp.Sort.NONE)

    def on_execute(self, item, action):
        Registry.execute(item, action)

    def on_events(self, flags):
        if flags & kp.Events.PACKCONFIG or flags & kp.Events.APPCONFIG:
            settings = self.load_settings()
            on_config_change({
                setting[0]: settings.get_stripped(setting[0], setting[1])
                for setting in self.configs
            })
        return
