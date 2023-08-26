import json

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
    def test_sort_brewery_by_type(self, brewery_type):
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

    def test_get_list_brewery(self):
        base_request = BaseRequest(url_data.BASE_URL_OPEN_BREWERY)
        response = base_request.get('')
        assert len(response) == 50

    @pytest.mark.parametrize('city', ['San Diego', 'Los Angeles'])
    def test_sort_brewery_by_city(self, city):
        base_request = BaseRequest(url_data.BASE_URL_OPEN_BREWERY)
        response = base_request.get(f'?by_city={city}&per_page=3')
        for brewery in response:
            assert city.lower() in brewery['city'].lower()


    def test_sotr_brewery_by_dist(self, generate_random_coordinates):
        base_request = BaseRequest(url_data.BASE_URL_OPEN_BREWERY)
        lon, lan = generate_random_coordinates
        response = base_request.get(f'?by_dist={lon},{lan}')
        assert len(response) != 0

        # добавить проверку что список отсортирован


