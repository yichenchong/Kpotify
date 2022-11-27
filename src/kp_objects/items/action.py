from abc import abstractmethod


class Action:
    def to_kp_action_dict(self):
        return {
            'name': self.name(),
            'label': self.label(),
            'short_desc': self.short_desc(),
            'data_bag': self.data_bag()
        }

    @abstractmethod
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def label(self):
        raise NotImplementedError

    @abstractmethod
    def short_desc(self):
        raise NotImplementedError

    @abstractmethod
    def data_bag(self):
        raise NotImplementedError

    def __str__(self):
        return self.label()

    def __repr__(self):
        return self.label()

    def __eq__(self, other):
        if isinstance(other, Action):
            return self.to_kp_action_dict() == other.to_kp_action_dict()
        if isinstance(other, dict):
            return self.to_kp_action_dict() == other
        if isinstance(other, str):
            return self.name() == other
        return False

    def __hash__(self):
        return hash(self.to_kp_action_dict())

    def __ne__(self, other):
        return not self.__eq__(other)
