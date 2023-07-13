import pytest

from src.rectangle import Rectangle


class TestRectangle:

    @pytest.mark.parametrize('side_a, side_b, expected_area',
                             [
                                 (1, 1, 1),
                                 (10, 20, 200),
                                 (999, 999, 998001),
                                 (0.1, 0.1, 0.01)
                             ])
    def test_rectangle_get_area(self, side_a, side_b, expected_area):
        rectangle = Rectangle(side_a, side_b)
        rectangle_area = rectangle.get_area()
        if type(rectangle_area) == float:
            rectangle_area = round(rectangle_area, 2)

        assert rectangle_area == expected_area

    @pytest.mark.parametrize('side_a, side_b, expected_perimeter',
                             [
                                 (1, 1, 4),
                                 (10, 20, 60),
                                 (999, 999, 3996),
                                 (0.1, 0.1, 0.4)
                             ])
    def test_rectangle_get_perimeter(self, side_a, side_b, expected_perimeter):
        rectangle = Rectangle(side_a, side_b)
        rectangle_perimeter = rectangle.get_perimeter()

        assert rectangle_perimeter == expected_perimeter

    @pytest.mark.parametrize('side_a, side_b',
                             [
                                 (1, 1),
                                 (10, 20),
                                 (999, 999),
                                 (0.1, 0.1)
                             ])
    def test_rectangle_creating(self, side_a, side_b):
        rectangle = Rectangle(side_a, side_b)
        name = rectangle.name

        assert name == 'Rectangle'

    @pytest.mark.parametrize('side_a, side_b',
                             [
                                 (-1, 1),
                                 (-10, -20),
                                 (0, 1),
                                 (-4, 0)
                             ])
    def test_rectangle_not_creating(self, side_a, side_b):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)
