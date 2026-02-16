from app.player import Player


class PlayerNode:
    def __init__(self, player=Player):
        self.next = None
        self.previous = None
        self.player = player
        self.key = self.player._uid

    def __str__(self):
        return "NEXT: {} | PREVIOUS: {} | KEY: {}".format(self.next, self.previous, self.key)

