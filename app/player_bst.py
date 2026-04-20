from app.player import Player


class PlayerBST:

    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: Player):
        self.__value = value
