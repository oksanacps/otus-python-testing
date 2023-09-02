import pytest

from src.base_request import BaseRequest
from test_data.url_data import BASE_URL_JSON_PLACEHOLDER


@pytest.fixture(scope='module')
def get_request_instance():
    request = BaseRequest(BASE_URL_JSON_PLACEHOLDER)
    yield request


@pytest.fixture(params=['1', '2'])
def get_post_by_id(request, get_request_instance):
    base_request = get_request_instance
    response = base_request.get(f'posts/{request.param}')

    yield response['title'], request.param, base_request
