from app.player import Player


class PlayerList:

    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def insert_first(self, new_player=Player):
        if self.is_empty():
            self.first = new_player
            return

        self.first._next = self.first
        self.first = new_player



