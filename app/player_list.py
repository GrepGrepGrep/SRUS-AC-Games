from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    _first: PlayerNode = None
    _last: PlayerNode = None

    def is_empty(self):
        return self._first is None

    def insert_first(self, new_player: Player):
        player_node = PlayerNode(new_player)

        if self.is_empty():
            self._first = player_node
            self._last = player_node
            return

        player_node.next = self._first
        self._first.previous = player_node
        self._first = player_node

    def insert_last(self, new_player: Player):
        player_node = PlayerNode(new_player)
        if self._first is None:
            self._first = player_node
            self._last = player_node
            return

        self._last.next = player_node
        player_node.previous = self._last
        self._last = player_node

    def delete_first(self):
        if self._first is None:
            return

        self._first = self._first.next
        if self._first is not None:
            self._first.previous = None

    def delete_last(self):
        if self._first is None:
            return

        last = self._last.previous
        last.next = None
        self._last = last

    def __str__(self):
        buf = "items: ["
        current = self._first

        while current is not None:
            buf += " " + str(current.player._name)
            # buf += str(current)
            current = current.next
        buf += " ]"
        return buf

    def delete_from_key(self, key: int):

        current = self._first

        while current is not None:
            if current.player._uid == key:
                if current.next is None and current.previous is None:
                    self._first = None
                    self._last = None
                    return
                if current == self._first:
                    self.delete_first()
                elif current == self._last:
                    self.delete_first()
                else:
                    previous = current.previous
                    next_1 = current.next

                    previous.next = next_1
                    next_1.previous = previous
                return
            current = current.next

    def display(self, forward=True):

        if forward:
            print(self.__str__())
            return

        # if backward

        buf = ""
        current = self._last
        while current is not None:
            buf += " " + str(current.player._name)
            current = current.previous

        print("items: [{} ]".format(buf))

    def get(self, key: int):
        current = self._last
        while current is not None and current.player._uid != key:
            current = current.previous
        return current

    def count(self):

        # print(self._last.display())
        num = 0
        current = self._last
        while current is not None:
            num += 1
            current = current.previous
        return num
