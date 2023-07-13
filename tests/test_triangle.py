import pytest

from src.triangle import Triangle


class TestTriangle:

    @pytest.mark.parametrize('side_a, side_b, side_c, expected_area',
                             [
                                 (5, 7, 10, 16.25),
                                 (7, 10, 12, 34.98),
                                 (0.6, 0.9, 1.4, 0.18)
                             ])
    def test_triangle_get_area(self, side_a, side_b, side_c, expected_area):
        triangle = Triangle(side_a, side_b, side_c)
        triangle_area = triangle.get_area()
        if type(triangle_area) == float:
            triangle_area = round(triangle_area, 2)

        assert triangle_area == expected_area

    @pytest.mark.parametrize('side_a, side_b, side_c, expected_perimeter',
                             [
                                 (5, 7, 10, 22),
                                 (7, 10, 12, 29),
                                 (0.6, 0.9, 1.4, 2.9)
                             ])
    def test_triangle_get_perimeter(self, side_a, side_b, side_c, expected_perimeter):
        triangle = Triangle(side_a, side_b, side_c)
        triangle_perimeter = triangle.get_perimeter()

        assert triangle_perimeter == expected_perimeter

    @pytest.mark.parametrize('side_a, side_b, side_c',
                             [
                                 (5, 7, 10),
                                 (7, 10, 12),
                                 (0.6, 0.9, 1.4)
                             ])
    def test_triangle_creating(self, side_a, side_b, side_c):
        triangle = Triangle(side_a, side_b, side_c)
        name = triangle.name

        assert name == 'Triangle'

    @pytest.mark.parametrize('side_a, side_b, side_c',
                             [
                                 (1, 2, 3),
                                 (3, 4, 8),
                                 (11, 15, 30)
                             ])
    def test_triangle_not_creating(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)
