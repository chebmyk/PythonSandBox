from classes.project3.inventory.model.inventory import Resource


class Storage(Resource):

    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB

    def __repr__(self):
        return f'{self.name} ({self.category})'


class HDD(Storage):

    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = interface
        self._rpm = rpm

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f'{self.name} ({self.category})'