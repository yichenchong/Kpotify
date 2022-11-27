from abc import abstractmethod
import keypirinha as kp


class Item:
    category = 0

    def to_kp_item_dict(self):
        if self.category == 0:
            raise NotImplementedError("Category not set")
        return {
            'category': self.category,
            'label': self.label(),
            'short_desc': self.description(),
            'target': self.target(),
            'args_hint': self.args_hint(),
            'hit_hint': self.hit_hint(),
            'loop_on_suggest': self.loop_on_suggest(),
            'icon_handle': self.icon_handle(),
            'data_bag': self.data_bag()
        }

    @abstractmethod
    def label(self):
        raise NotImplementedError

    @abstractmethod
    def description(self):
        raise NotImplementedError

    @abstractmethod
    def target(self):
        raise NotImplementedError

    def args_hint(self):
        return kp.ItemArgsHint.FORBIDDEN

    def hit_hint(self):
        return kp.ItemHitHint.NOARGS

    def loop_on_suggest(self):
        return False

    @abstractmethod
    def icon_handle(self):
        raise NotImplementedError

    @abstractmethod
    def data_bag(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def execute(item, action):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def actions():
        raise NotImplementedError

    def __str__(self):
        return self.label()

    def __repr__(self):
        return self.label()

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.to_kp_item_dict() == other.to_kp_item_dict()
        if isinstance(other, dict):
            return self.to_kp_item_dict() == other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(tuple(sorted(self.to_kp_item_dict().items())))