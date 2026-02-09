# https://docs.python.org/3/library/unittest.html

import unittest

from app.player import Player


class TestPlayerMethods(unittest.TestCase):

    def test_init_name(self):
        name = "ava"
        uid = "903584930"

        player = Player(name=name, uid=uid)

        self.assertEqual(player._name, name)

    def test_init_uid(self):
        name = "ava"
        uid = "903584930"

        player = Player(name=name, uid=uid)

        self.assertEqual(player._uid, uid)
