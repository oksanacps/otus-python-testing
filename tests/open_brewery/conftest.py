import random
import pytest


@pytest.fixture
def generate_random_coordinates():
    min_lat = -90.0
    max_lat = 90.0
    min_lon = -180.0
    max_lon = 180.0

    random_lat = random.uniform(min_lat, max_lat)
    random_lon = random.uniform(min_lon, max_lon)

    longitude = "{:.7f}".format(random_lon)
    latitude = "{:.7f}".format(random_lat)

    return longitude, latitude
