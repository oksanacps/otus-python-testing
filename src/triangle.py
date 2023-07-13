from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError(
                f'It is impossible to create a triangle with side lengths {side_a} and {side_b} and {side_c}')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        square = sqrt(semi_perimeter
                      * (semi_perimeter - self.side_a)
                      * (semi_perimeter - self.side_b)
                      * (semi_perimeter - self.side_c))
        return square

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
