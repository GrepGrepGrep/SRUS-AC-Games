import unittest

from app.player import Player
from app.player_list import PlayerList


class TestPlayerListMethods(unittest.TestCase):

    def test_insert_first_populated(self):


        plist = PlayerList()
        plist.insert_first(Player(_uid=3439, _name="ava"))
        plist.insert_first(Player(_uid=304, _name="steve"))

        self.assertEqual(plist._first.player._name, "steve")

    def test_last_populated(self):
        plist = PlayerList()

        plist.insert_first(Player(_uid=3439, _name="ava"))
        plist.insert_last(Player(_uid=304, _name="steve"))

        plist.insert_first(Player(_uid=345443, _name="bob"))


       # self.assertEqual(plist._first._player._name, "steve")
        print(plist)


        self.assertEqual(plist._first.player._name, "bob")

        self.assertEqual(plist._last.player._name, "steve")


    def test_insert_first_empty(self):
        player_ava = Player(_uid=3439, _name="ava")
        plist = PlayerList()


        self.assertTrue(plist.is_empty())

        plist.insert_first(player_ava)
        self.assertEqual(plist._first.player._name, "ava")
