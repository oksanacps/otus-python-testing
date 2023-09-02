import random
import pytest

from src.base_request import BaseRequest
from test_data.url_data import BASE_URL_OPEN_BREWERY


@pytest.fixture(scope='module')
def get_request_instance():
    request = BaseRequest(BASE_URL_OPEN_BREWERY)
    yield request


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
