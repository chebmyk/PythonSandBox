
from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CORTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y, system = CoordinateSystem.CORTESIAN):
        self.x = x
        self.y = y
        self.system = system


    @staticmethod
    def new_cortisian_point(x, y):
        return Point(x,y, system=CoordinateSystem.CORTESIAN)


    @staticmethod
    def new_polar_point(x, y):
        return Point(x * cos(y), x * sin(y), system=CoordinateSystem.POLAR)

    def __str__(self):
        return  f"Point(x={self.x},y={self.y},system={self.system})"




cp = Point.new_cortisian_point(1,5)

print(cp)

pp = Point.new_polar_point(1,5)

print(pp)