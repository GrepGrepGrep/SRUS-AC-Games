from app.player import Player


class PlayerNode:
    def __init__(self, player=Player):
        self.next = None
        self.previous = None
        self.player = player
        self.key = self.player.uid

    def __str__(self):
        print("NEXT: {} | PREVIOUS: {} | KEY: {}".format(self.next, self.previous, self.key))
