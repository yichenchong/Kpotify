import unittest

from ...src.spotify_wrapper import Player

class TestManual ( unittest . TestCase ):
    def test_manual(self):
        print(Player.play().request.__dict__)