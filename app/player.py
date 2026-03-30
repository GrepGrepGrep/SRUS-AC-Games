# https://machinelearningplus.com/python/python-property-getters-setters-and-attribute-control-guide/

def score_validate(score):
    if score < 0:
        raise ValueError('Invalid value, positive scores only')


class Player:

    def __init__(self, _uid: str, _name: str, _score: int = 0) -> None:
        score_validate(_score)
        self._uid = _uid
        self._name = _name
        self._score = _score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score: int = 0):
        score_validate(score)
        self._score = score

    def __str__(self):
        return "UID: {} | name: {}".format(self._uid, self._name)

    def __eq__(self, other):
        return self._uid == other._uid


    def __gt__(self, other):
        return self._score > other._score

    def sort_quickly(self, arr: list[Player]):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:
                right.append(x)
            else:

                left.append(x)
        return self.sort_quickly(left) + [pivot] + self.sort_quickly(right)