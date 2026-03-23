# https://docs.python.org/3/library/unittest.html

import unittest

from app.player import Player
from app.player_hashmap import PlayerHashMap


def data():
    p = PlayerHashMap(10)
    print("aaaa {}".format(len(p.table)))
    p.put(Player(_uid=11, _name="bob"))
    p.put(Player(_uid=1, _name="ava"))
    p.put(Player(_uid=20, _name="dave"))
    p.put(Player(_uid=10, _name="steve"))
    return p


class TestPlayerMethods(unittest.TestCase):

    def test_uid(self):
        p = data()
        p.put(Player(_uid=11, _name="bob_again"))
        # length should be 4
        self.assertEqual(p.len(), 4)


    def test_get_none(self):
        p = data()
        self.assertIsNone(p.get(124))

    def test_get(self):
        p = data()
        self.assertIsNotNone(p.get(11))

    def test_remove(self):
        p = data()
        self.assertIsNotNone(p.get(11))
        p.remove(11)
        self.assertIsNone(p.get(11))

    def test_len(self):

        p = data()
        print(p)
        self.assertEqual(p.len(), 4)
        # p.remove(11)
        p.remove(1)
        print("aaa")
        print(p)
        p.remove(11)
        self.assertEqual(p.len(), 2)
