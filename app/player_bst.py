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
            else:
                self.__insert_inner(player, node.left)
        else:
            if node.right is None:
                node.right = PlayerBNode(player)

            else:
                self.__insert_inner(player, node.right)

    def __search_inner(self, name: str, node: PlayerBNode) -> bool:
        if name == node.root._name:
            return True

        if name < node.root._name:
            if node.left is None:
                # node.left = PlayerBNode(player)
                return False
            else:
                self.__search_inner(name, node.left)
        else:
            if node.right is None:
                # node.right = PlayerBNode(player)
                return False

            else:
                self.__search_inner(name, node.right)

    def search(self, name: str) -> bool:
        return self.__search_inner(name, self.value)

    def to_list(self):

        items = []
        self.__through(self.value, items)
        items.sort()
        list_new = PlayerBST()
        list_new.value = items.pop(len(items) // 2)
        for item in items:
            list_new.insert(item)

        self.value = list_new.value.root

    def __through(self, node: PlayerBNode, items: list):

        if node.left is not None:
            self.__through(node.left, items)
        if node.right:
            self.__through(node.right, items)
        items.append(node.root)
