class Player:

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name


    def __str__(self):
        print("UID: {} | name: {}" .format(self.uid, self.name))