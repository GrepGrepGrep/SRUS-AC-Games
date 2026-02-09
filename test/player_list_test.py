import unittest

from app.player import Player
from app.player_list import PlayerList


class TestPlayerListMethods(unittest.TestCase):

    def test_insert_first_populated(self):
        player_ava = Player(uid=3439, name="ava")
        player_steve = Player(uid=304, name="steve")
        plist = PlayerList()
        plist.insert_first(player_ava)


        plist.insert_first(player_steve)

        self.assertEqual(plist.first._name, "steve")

    def test_insert_first_empty(self):
        player_ava = Player(uid=3439, name="ava")
        plist = PlayerList()


        self.assertTrue(plist.is_empty())

        plist.insert_first(player_ava)
        self.assertEqual(plist.first._name, "ava")
