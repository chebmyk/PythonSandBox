from classes.project3.inventory.utils.validators import int_validator


class Resource:
    """ Base Class"""

    def __init__(self, name, manufacturer, total, allocated ):
        self._name = name
        self._manufacturer = manufacturer

        int_validator('total', total, 0)
        self._total = total
        int_validator('allocated', allocated, 0, total)
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated


    @property
    def category(self):
        return self.__class__.__name__

    @property
    def available(self):
        return self.total - self.allocated


    def __str__(self):
        return f'{self.name}'


    def __repr__(self):
        return f'{self.name} ({self.category})'


    def claim(self, number):
        int_validator('number', number, 1, self.available)
        self._allocated += number


    def freeup(self, number):
        int_validator('number', number, 1, self.allocated)
        self._allocated -= number


    def remove(self, number):
        int_validator('number', number, 1, self.total)
        self._total -= number
        self._allocated -= number


    def purchase(self, number):
        int_validator('number', number, 1)
        self._total += number