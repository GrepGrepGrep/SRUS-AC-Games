from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:

    def __init__(self):
        # type PlayerBNode
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, player: Player):
        self.__value = PlayerBNode(player)

    def insert(self, player: Player):
        self.__insert_inner(player, self.value)

    def __insert_inner(self, player: Player, node: PlayerBNode):

        if player._name == node.root._name:
            return

        if player._name < node.root._name:
            if node.left is None:
                node.left = PlayerBNode(player)
                return
            else:
                self.__insert_inner(player, node.left)
        else:
            if node.right is None:
                node.right = PlayerBNode(player)
                return
            else:
                self.__insert_inner(player, node.right)




