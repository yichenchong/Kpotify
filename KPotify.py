from src.logger import debug
from .src.kp_objects import Registry
from .src.config_handler import on_config_change
from .src.parsing_client import parse as Parse
from .src.kp_objects.image_downloader import ImageDownloader
import keypirinha as kp


class KPotify(kp.Plugin):
    """
    A KeyPirinha plugin to control Spotify
    """
    handles = []

    str_configs = [
        ("client_id", "spotify"),
        ("client_secret", "spotify"),
        ("device_id", "device")
    ]

    bool_configs = [
        ("load_icons", "preferences")
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
        config_dict = {
            setting[0]: settings.get_stripped(setting[0], setting[1])
            for setting in self.str_configs
        }
        config_dict.update({
            setting[0]: settings.get_bool(setting[0], setting[1])
            for setting in self.bool_configs
        })
        on_config_change(config_dict)

    def on_catalog(self):
        return

    def on_deactivated(self):
        while KPotify.handles:
            handle = KPotify.handles.pop()
            handle.free()
        ImageDownloader.clear()

    def on_suggest(self, user_input, items_chain):
        if not user_input.startswith("kpot"):
            return
        suggested_items = Parse.parse(user_input)
        if suggested_items is None or suggested_items == []:
            return
        self.set_suggestions([
            self.create_item(
                **self.parse_kp_item_dict(
                    item.to_kp_item_dict()
                )
            )
            for item in suggested_items
        ], kp.Match.ANY, kp.Sort.NONE)

    def on_execute(self, item, action):
        Registry.execute(item, action)

    def on_events(self, flags):
        debug("Detected config change in KPotify, reloading config")
        settings = self.load_settings()
        config_dict = {
            setting[0]: settings.get_stripped(setting[0], setting[1])
            for setting in self.str_configs
        }
        config_dict.update({
            setting[0]: settings.get_bool(setting[0], setting[1])
            for setting in self.bool_configs
        })
        on_config_change(config_dict)

    def parse_kp_item_dict(self, item_dict):
        icon_handle_result = item_dict["icon_handle"].result()
        if kp.should_terminate():
            item_dict["icon_handle"] = None
            return item_dict
        if icon_handle_result is not None:
            try:
                item_dict["icon_handle"] = self.load_icon(icon_handle_result)
                KPotify.handles.append(item_dict["icon_handle"])
            except ValueError:
                item_dict["icon_handle"] = None
        else:
            item_dict["icon_handle"] = None
        return item_dict
