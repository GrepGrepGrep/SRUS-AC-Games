# PlayerHashMap<PlayerList<Player>>;
# https://stackoverflow.com/questions/6142689/initialising-an-array-of-fixed-size-in-python
# https://docs.python.org/3/library/unittest.html

from app.player_list import PlayerList
from app.player import Player


# WIP: key equals index
# todo: implement hash function

class PlayerHashMap:
    # SIZE: int = 10
    SEED: int = 43840983043
    size: int = None
    table: list = []

    def __init__(self, size: int):
        self.size = size
        for x in range(0, size):
            self.table.append(PlayerList())

    def __str__(self):
        buf = ""
        len = 0
        for x in self.table:
            buf += "\n{1} {0}".format(x, len)
            len += 1
        return buf

    def display(self):
        buf = ""
        len = 0
        for x in self.table:
            if x.is_empty():
                continue
            buf += "\n{1} {0}".format(x, len)
            len += 1
        return buf

    def hash(self, key: int):
        return key % 10

    def put(self, player: Player):

        if self.get(player._uid) is not None:
            self.remove(player._uid)

        self.table[self.hash(player._uid)].insert_last(player)

    def get(self, key: int):

        return self.table[self.hash(key)].get(key)

    def remove(self, key: int):
        self.table[self.hash(key)].delete_from_key(key)

    def len(self):
        num = 0

        for table in self.table:
            num += table.count()
        return num
