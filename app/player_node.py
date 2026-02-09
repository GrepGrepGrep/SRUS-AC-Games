from app.player import Player


class PlayerNode:
    def __init__(self, player=Player):
        self._next = None
        self._previous = None
        self._player = player
        self.key = self._player._uid

    def __str__(self):
        print("NEXT: {} | PREVIOUS: {} | KEY: {}".format(self._next, self._previous, self.key))
