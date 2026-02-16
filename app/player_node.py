from app.player import Player


class PlayerNode:
    def __init__(self, player=Player):
        self.next = None
        self.previous = None
        self.player = player


    def display(self):
        next_p = self.next
        previous = self.previous
        if next_p is not None:
            next_p = next_p.player._name;

        if previous is not None:
            previous = previous.player._name;
        print("------------------------------------")
        print("previous | current | next")
        print("{} <- {} -> {}".format( previous, self.player._name,  next_p,))
        print("------------------------------------")