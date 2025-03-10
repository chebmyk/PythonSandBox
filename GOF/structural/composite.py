class Sum:

    @property
    def sum(self):
        summ = 0
        for v in self:
            summ += v
        return summ

    def __radd__(self, val):
        return val + self.sum

    def __add__(self, val):
        return val + self.sum



class SingleValue(Sum):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, Sum): pass









