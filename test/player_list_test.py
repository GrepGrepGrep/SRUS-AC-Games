import unittest

from app.player import Player
from app.player_list import PlayerList


class TestPlayerListMethods(unittest.TestCase):

    def test_insert_first_populated(self):


        plist = PlayerList()
        plist.insert_first(Player(uid=3439, name="ava"))
        plist.insert_first(Player(uid=304, name="steve"))

        self.assertEqual(plist.first.player.name, "steve")

    def test_last_populated(self):
        plist = PlayerList()
        plist.insert_first(Player(uid=3439, name="ava"))
        plist.insert_last(Player(uid=304, name="steve"))
        plist.insert_first(Player(uid=345443, name="bob"))

       # self.assertEqual(plist._first._player._name, "steve")

        self.assertEqual(plist.first.player.name, "ava")

        self.assertEqual(plist.last.player.name, "steve")


    def test_insert_first_empty(self):
        player_ava = Player(uid=3439, name="ava")
        plist = PlayerList()


        self.assertTrue(plist.is_empty())

        plist.insert_first(player_ava)
        self.assertEqual(plist.first.player.name, "ava")
