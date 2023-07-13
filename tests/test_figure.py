import pytest

from src.triangle import Triangle
from src.circle import Circle
from src.square import Square
from src.rectangle import Rectangle

rectangle = Rectangle(1, 2)
circle = Circle(90)
triangle = Triangle(7, 10, 12)
square = Square(11)
test_str = 'str'
test_number = 123
test_list = []


class TestFigure:

    @pytest.mark.parametrize('figure, other_figure, expected_area', [
        (rectangle, triangle, 37),
        (square, circle, 25568),
        (square, triangle, 156),
        (rectangle, circle, 25449),
        (rectangle, square, 123)
    ])
    def test_add_area(self, figure, other_figure, expected_area):
        total_area = round(figure.add_area(other_figure))

        assert total_area == expected_area

    @pytest.mark.parametrize('figure, other_figure', [
        (circle, test_str),
        (circle, test_number),
        (circle, test_list)
    ])
    def test_add_area_not_figure(self, figure, other_figure):
        with pytest.raises(ValueError):
            figure.add_area(other_figure)
