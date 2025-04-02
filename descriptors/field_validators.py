import numbers

class MinMaxValidator:
    def __init__(self, min_= None, max_ = None):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner, name):
        self._name = name

    def validate(self, value):
        pass

    def __set__(self, instance, value):
        # Validate the value before setting it
        self.validate(value)
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self._name, None)


class IntegerField(MinMaxValidator):

    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self._name} must be an integer')
        if value < self._min:
            raise ValueError(f'{self._name} must be greater than or equal to {self._min}')
        if value > self._max:
            raise ValueError(f'{self._name} must be less than or equal to {self._max}')




class CharField(MinMaxValidator):

    def __init__(self, min_= None, max_ = None):
        min_ = min_ or 0
        min_ = max(min_, 0)  # Ensure min_ is at least 0
        super().__init__(min_, max_)  # Call the parent constructor to initialize min and max


    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self._name} must be an string')
        if len(value) < self._min:
            raise ValueError(f'{self._name} must be greater than or equal to {self._min}')
        if len(value) > self._max:
            raise ValueError(f'{self._name} must be less than or equal to {self._max}')


