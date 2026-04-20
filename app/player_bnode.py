from app.player import Player


class PlayerBNode:

    def __init__(self, root: Player):
        self.__root = root
        self.__left = None
        self.__right = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value: Player):
        self.__root = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value: Player):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value: Player):
        self.__right = value