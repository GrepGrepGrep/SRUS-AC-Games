class Player:

    def __init__(self, _uid: int, _name: str, _score: int):
        self._uid = _uid
        self._name = _name
        self._score = _score


    def __str__(self):
        return "UID: {} | name: {}" .format(self._uid, self._name)
