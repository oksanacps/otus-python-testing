from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __int__(self, side_a):
        if side_a <= 0:
            raise ValueError(f'It is impossible to create a square with side lengths {side_a}')
        self.side_a = side_a

    def get_square(self):
        return self.side_a ** 2

    def get_perimeter(self):
        return self.side_a * 4


