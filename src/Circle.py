from src.Figure import Figure
from math import pi


class Circle(Figure):
    name = 'Circle'

    def __int__(self, radius):
        if radius <= 0:
            raise ValueError(f'It is impossible to create a circle with {radius} radius')
        self.radius = radius

    def get_square(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius
