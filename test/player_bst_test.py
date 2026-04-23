# https://docs.python.org/3/library/unittest.html

import unittest

from app.player import Player
from app.player_bst import PlayerBST
from app.player_hashmap import PlayerHashMap


# def data():


class TestPlayerMethods(unittest.TestCase):

    def data(self) -> PlayerBST:
        b = PlayerBST()
        b.value = Player("0", "3", 5)
        b.insert(Player("0", "2", 5))
        b.insert(Player("0", "1", 1))
        b.insert(Player("0", "4", 4))
        b.insert(Player("0", "5", 1))
        return b

    def test_duplication(self):
        b = PlayerBST()

        b.value = Player("0", "3", 5)
        b.insert(Player("0", "3", 5))

        self.assertIsNotNone(b.value.root)
        self.assertIsNone(b.value.left)
        self.assertIsNone(b.value.right)

    def test_values(self):
        b = self.data()

        print(b.value.root._name)

        print(b.value.left.root._name)
        print(b.value.left.left.root._name)

        print(b.value.right.root._name)
        print(b.value.right.right.root._name)

        self.assertIs(b.value.root._name, "3")
        self.assertIs(b.value.left.root._name, "2")
        self.assertIs(b.value.left.left.root._name, "1")
        self.assertIs(b.value.right.root._name, "4")
        self.assertIs(b.value.right.right.root._name, "5")

    def test_search(self):
        b = self.data()
        self.assertTrue(b.search("3"))
        self.assertFalse(b.search("WOMP"))
