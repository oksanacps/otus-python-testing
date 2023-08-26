import pytest

from src.base_request import BaseRequest
from test_data.url_data import BASE_URL_DOG_CEO


@pytest.fixture(scope='module')
def get_request_instance():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    request = BaseRequest(BASE_URL_DOG_CEO, headers)
    yield request
