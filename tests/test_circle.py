import pytest

from src.circle import Circle


class TestCircle:

    @pytest.mark.parametrize('radius, expected_area',
                             [
                                 (1, 3.14),
                                 (10, 314.16),
                                 (999, 3135312.61),
                                 (0.1, 0.03)
                             ])
    def test_circle_get_area(self, radius, expected_area):
        circle = Circle(radius)
        circle_area = round(circle.get_area(), 2)

        assert circle_area == expected_area

    @pytest.mark.parametrize('radius, expected_perimeter',
                             [
                                 (1, 6.28),
                                 (10, 62.83),
                                 (999, 6276.90),
                                 (0.1, 0.63)
                             ])
    def test_circle_get_perimeter(self, radius, expected_perimeter):
        circle = Circle(radius)
        circle_perimeter = round(circle.get_perimeter(), 2)

        assert circle_perimeter == expected_perimeter

    @pytest.mark.parametrize('radius', [1, 10, 999, 0.1])
    def test_circle_creating(self, radius):
        circle = Circle(radius)
        name = circle.name

        assert name == 'Circle'

    @pytest.mark.parametrize('radius', [-1, 0])
    def test_circle_not_creating(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)
