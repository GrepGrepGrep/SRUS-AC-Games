

from app.player import Player
from app.player_node import PlayerNode


class PlayerList:




    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def insert_first(self, new_player=Player):
        player_node =  PlayerNode(new_player)

        if self.is_empty():
            self.first = player_node
            self.last = player_node
            return


        self.first._previous = player_node
        player_node.next = self.first
        self.first = player_node

    def insert_last(self, new_player=Player):
        player_node = PlayerNode(new_player)

        if self.first is None:
            self.first = player_node
            self.last = player_node
            return

        player_node._previous = self.last
        self.last.next = player_node
        self.last = player_node









