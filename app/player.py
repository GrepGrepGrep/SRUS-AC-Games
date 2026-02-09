class Player:

    def __init__(self, uid, name):
        self._uid = uid
        self._name = name


    def __str__(self):
        print("UID: {} | name: {}" .format(self._uid, self._name))