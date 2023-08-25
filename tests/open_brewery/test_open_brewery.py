import pytest

from src.base_request import BaseRequest
from test_data import url_data


@pytest.mark.brewery
class TestOpenBrewery:
    """

    """
    @pytest.mark.parametrize('brewery_type', [
        'micro',
        'nano',
        'regional',
        'brewpub',
        'large',
        'planning',
        'contract',
        'proprietor',
        'closed'
    ])
    def test_brewery_type(self, brewery_type):
        base_request = BaseRequest(url_data.BASE_URL_OPEN_BREWERY)
        response = base_request.get(f'?by_type={brewery_type}&per_page=3')
        for brewery in response:
            assert brewery['brewery_type'] == brewery_type

    @pytest.mark.parametrize('search', ['dog', 'GREEN'])
    def test_search_not_case_sensitive(self, search):
        base_request = BaseRequest(url_data.BASE_URL_OPEN_BREWERY)
        response = base_request.get(f'search?query={search}&per_page=3')
        for brewery in response:
            assert search.lower() in brewery['name'].lower()
        # скорее всего если регистрозависимость, то нужно с одним именем найти и сравнить что нашлось одинковое

    def test_open_brewery3(self):
        pass

    @pytest.mark.parametrize('example', [1, 2])
    def test_open_brewery4(self, example):
        pass

    @pytest.mark.parametrize('example', [1, 2])
    def test_open_brewery5(self, example):
        pass