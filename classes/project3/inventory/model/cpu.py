from classes.project3.inventory.model.inventory import Resource
from classes.project3.inventory.utils.validators import int_validator


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        int_validator('cores', cores, 1)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return f'{self.name} ({self.category})'
    