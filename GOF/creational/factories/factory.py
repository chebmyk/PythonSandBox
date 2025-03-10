from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y, system = CoordinateSystem.CARTESIAN):
        self.x = x
        self.y = y
        self.system = system


    @staticmethod
    def new_cortisian_point(x, y):
        return Point(x, y, system=CoordinateSystem.CARTESIAN)


    @staticmethod
    def new_polar_point(x, y):
        return Point(x * cos(y), x * sin(y), system=CoordinateSystem.POLAR)

    def __str__(self):
        return  f"Point(x={self.x},y={self.y},system={self.system})"



class PointFactory:

    @staticmethod
    def new_cortisian_point(x, y):
        return Point(x, y, system=CoordinateSystem.CARTESIAN)


    @staticmethod
    def new_polar_point(x, y):
        return Point(x * cos(y), x * sin(y), system=CoordinateSystem.POLAR)
