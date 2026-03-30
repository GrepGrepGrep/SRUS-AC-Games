# https://docs.python.org/3/library/unittest.html

import unittest

from app.player import Player




class TestPlayerMethods(unittest.TestCase):

    def test_init_name(self):
        name = "ava"
        uid = "903584930"

        player = Player(_name=name, _uid=uid)

        self.assertEqual(player._name, name)

    def test_init_uid(self):
        name = "ava"
        uid = "903584930"

        player = Player(_name=name, _uid=uid)

        self.assertEqual(player._uid, uid)

    def test_sort_players(self):
        players = [Player(_name="Alice", _uid='01', _score=10), Player(_name="Bob", _uid='02', _score=5),
                   Player(_name="Charlie", _uid='03', _score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(_name="Bob", _uid='02', _score=5), Player(_name="Alice", _uid='01', _score=10),
                                   Player(_name="Charlie", _uid='03', _score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(_name="Alice", _uid='01', _score=10)
        bob = Player(_name="Bob", _uid='02', _score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice > bob )
        # or, event better
        self.assertGreater(alice, bob)