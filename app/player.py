class Player:

    def __init__(self, _uid, _name):
        self._uid = _uid
        self._name = _name


    def __str__(self):
        print("UID: {} | name: {}" .format(self._uid, self._name))