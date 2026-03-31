# https://docs.python.org/3/library/unittest.html
import random
import time
import unittest

from more_itertools.more import is_sorted
from numpy.ma.testutils import assert_equal

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
        manually_sorted_players = [Player(_name="Bob", _uid='02', _score=5),
                                   Player(_name="Alice", _uid='01', _score=10),
                                   Player(_name="Charlie", _uid='03', _score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(_name="Alice", _uid='01', _score=10)
        bob = Player(_name="Bob", _uid='02', _score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice > bob)
        # or, event better
        self.assertGreater(alice, bob)

    def test_score_sort(self):
        players = [Player(_name="Alice", _uid='01', _score=10), Player(_name="Bob", _uid='02', _score=5),
                   Player(_name="Charlie", _uid='03', _score=15)]

        algo_sorted = Player("0", "NULL").sort_quickly(arr=players)


        self.assertTrue(is_sorted(algo_sorted, reverse=True))

    def test_sort_against_std(self):
        import random

        players = [Player(_name=f"Player {i}", _uid=f"{i:03}", _score=random.randint(0, 1000)) for i in range(1000)]

        sort = sorted(players)
        sort.reverse()

        self.assertTrue(is_sorted(sort, reverse=True))
        self.assertTrue(is_sorted(Player("0", "NULL").sort_quickly(arr=players), reverse=True))

    def test_already_sorted(self):
        import random

        players = [Player(_name=f"Player {i}", _uid=f"{i:03}", _score=random.randint(0, 1000)) for i in range(1000)]

        my_sorted = Player("0", "NULL").sort_quickly(arr=players)


        self.assertTrue(is_sorted(my_sorted, reverse=True))

    def test_drag_race_pivot(self):
        import sys
        sys.setrecursionlimit(1500)

        def sort_quickly(arr: list[Player]):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left = []
            right = []
            for x in arr[1:]:
                if x < pivot:
                    right.append(x)
                else:
                    left.append(x)
            return sort_quickly(left) + [pivot] + sort_quickly(right)

        def sort_quickly_middle(arr: list[Player]):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = []
            right = []
            for x in arr[1:]:
                if x < pivot:
                    right.append(x)
                else:
                    left.append(x)
            return sort_quickly(left) + [pivot] + sort_quickly(right)

        players = [Player(_name=f"Player {i}", _uid=f"{i:03}", _score=random.randint(0, 1000)) for i in range(1000)]
        players_sorted = sorted(players)

        print("unsorted | middle")
        for x in range(0, 3):
            start = time.time()
            sort_quickly_middle(players)
            end = time.time()
            print(end - start)

        print("unsorted | start")
        for x in range(0, 3):
            start = time.time()
            sort_quickly(players)
            end = time.time()
            print(end - start)

        print("sorted | middle")
        for x in range(0, 3):
            start = time.time()
            sort_quickly_middle(players_sorted)
            end = time.time()
            print(end - start)

        print("sorted | start")
        for x in range(0, 3):
            start = time.time()
            sort_quickly(players_sorted)
            end = time.time()
            print(end - start)
