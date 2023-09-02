import pytest

from tests.open_brewery import helpers


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
        response = base_request.get(params={'by_type': brewery_type})
        for brewery in response:
            assert brewery['brewery_type'] == brewery_type

    @pytest.mark.parametrize('lower_search, upper_search', [('dog', 'Dog'), ('GREEN', 'green')])
    def test_search_not_case_sensitive(self, lower_search, upper_search, get_request_instance):
        base_request = get_request_instance
        lower_search_result = base_request.get(endpoint='search', params={'query': lower_search})
        upper_search_result = base_request.get(endpoint='search', params={'query': upper_search})
        assert lower_search_result == upper_search_result

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

    def test_sort_brewery_by_dist(self, generate_random_coordinates, get_request_instance):
        base_request = get_request_instance
        lon, lat = generate_random_coordinates
        dist = f'{lon},{lat}'
        response = base_request.get(params={'by_dist': dist})
        lon1, lat1 = float(lon), float(lat)
        lon2, lat2 = float(response[0]['longitude']), float(response[0]['latitude'])
        distance1 = helpers.haversine_distance(lon1, lat1, lon2, lat2)
        for brewery in range(1, len(response)):
            lon2, lat2 = float(response[brewery]['longitude']), float(response[brewery]['latitude'])
            distance2 = helpers.haversine_distance(lon1, lat1, lon2, lat2)
            assert distance1 <= distance2
            distance1 = distance2
