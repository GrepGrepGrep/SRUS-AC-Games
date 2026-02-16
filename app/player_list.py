from app.player import Player
from app.player_node import PlayerNode


class PlayerList:

    def __init__(self):
        self._first = None
        self._last = None

    def is_empty(self):
        return self._first is None

    def insert_first(self, new_player=Player):
        player_node = PlayerNode(new_player)

        if self.is_empty():
            self._first = player_node
            self._last = player_node
            return

        player_node.next = self._first
        self._first.previous = player_node
        self._first = player_node

    def insert_last(self, new_player=Player):
        player_node = PlayerNode(new_player)

        if self._first is None:
            self._first = player_node
            self._last = player_node
            return

        self._last.next = player_node
        player_node.previous = self._last
        self._last = player_node

    def __str__(self):
        buf = "items: ["
        current = self._first

        while current is not None:
            buf += " " + str(current.player._name)
            # buf += str(current)
            current = current.next
        buf += " ]"
        return buf
