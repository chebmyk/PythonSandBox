from abc import ABC

class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'Circle R={self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Square side={self.side}'


class ColorodShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'Shape of {self.shape} color = {self.color}'




circle = Circle(3)
red_circle = ColorodShape(circle, 'Red')


print(circle)
print(red_circle)