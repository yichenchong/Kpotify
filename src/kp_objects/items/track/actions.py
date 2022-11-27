from ..action import Action


class PlayTrack(Action):
    def name(self):
        return 'play_track'

    def label(self):
        return 'Play'

    def short_desc(self):
        return 'Play the track'

    def data_bag(self):
        return ""


class AddToQueue(Action):
    def name(self):
        return 'add_to_queue'

    def label(self):
        return 'Add to queue'

    def short_desc(self):
        return 'Add the track to the queue'

    def data_bag(self):
        return ""
