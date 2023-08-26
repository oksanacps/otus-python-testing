import pytest


@pytest.mark.brewery
class TestOpenBrewery:
    """

    """

    @pytest.mark.parametrize('brewery_type', [
        'micro',
        'planning',
        'closed'
    ])
    def test_sort_brewery_by_type(self, brewery_type, get_request_instance):
        base_request = get_request_instance
        response = base_request.get(params={'by_type': brewery_type})     #f'?by_type={brewery_type}&per_page=3'
        for brewery in response:
            assert brewery['brewery_type'] == brewery_type

    @pytest.mark.parametrize('search', ['dog', 'GREEN'])
    def test_search_not_case_sensitive(self, search, get_request_instance):
        base_request = get_request_instance
        response = base_request.get(endpoint='search', params={'query': search, 'per_page': '3'})
        for brewery in response:
            assert search.lower() in brewery['name'].lower()
        # скорее всего если регистрозависимость, то нужно с одним именем найти и сравнить что нашлось одинковое

    def test_get_list_brewery(self, get_request_instance):
        base_request = get_request_instance
        response = base_request.get()
        assert len(response) == 50

    @pytest.mark.parametrize('city', ['San Diego', 'Los Angeles'])
    def test_sort_brewery_by_city(self, city, get_request_instance):
        base_request = get_request_instance
        response = base_request.get(params={'by_city': city, 'per_page': '3'})
        for brewery in response:
            assert city.lower() in brewery['city'].lower()

    def test_sotr_brewery_by_dist(self, generate_random_coordinates, get_request_instance):
        base_request = get_request_instance
        lon, lan = generate_random_coordinates
        dist = f'{lon},{lan}'
        response = base_request.get(params={'by_dist': dist})
        assert len(response) != 0

        # добавить проверку что список отсортирован
