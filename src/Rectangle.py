from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'

    def __int__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'It is impossible to create a rectangle with side lengths {side_a} and {side_b}')
        self.side_a = side_a
        self.side_b = side_b

    def get_square(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

