import pytest

from src.square import Square


class TestSquare:

    @pytest.mark.parametrize('side_a, expected_area',
                             [
                                 (1, 1),
                                 (10, 100),
                                 (999, 998001),
                                 (0.1, 0.01)
                             ])
    def test_square_get_area(self, side_a, expected_area):
        square = Square(side_a)
        square_area = square.get_area()
        if type(square_area) == float:
            square_area = round(square_area, 2)

        assert square_area == expected_area

    @pytest.mark.parametrize('side_a, expected_perimeter',
                             [
                                 (1, 4),
                                 (10, 40),
                                 (999, 3996),
                                 (0.1, 0.4)
                             ])
    def test_square_get_perimeter(self, side_a, expected_perimeter):
        square = Square(side_a)
        square_perimeter = square.get_perimeter()

        assert square_perimeter == expected_perimeter

    @pytest.mark.parametrize('side_a', [1, 10, 999, 0.1])
    def test_square_creating(self, side_a):
        square = Square(side_a)
        name = square.name

        assert name == 'Square'

    @pytest.mark.parametrize('side_a', [-1, 0])
    def test_square_not_creating(self, side_a):
        with pytest.raises(ValueError):
            Square(side_a)
