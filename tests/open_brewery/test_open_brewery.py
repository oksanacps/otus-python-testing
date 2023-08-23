import pytest

from src.base_request import BaseRequest


@pytest.mark.brewery
class TestOpenBrewery:
    """

    """

    def test_open_brewery1(self):
        base_request = BaseRequest(test_data.BASE_URL_DOG_CEO)
        response = base_request.get('example', 1)
        assert response.ok

    def test_open_brewery2(self):
        pass

    def test_open_brewery3(self):
        pass

    @pytest.mark.parametrize('example', [1, 2])
    def test_open_brewery4(self, example):
        pass

    @pytest.mark.parametrize('example', [1, 2])
    def test_open_brewery5(self, example):
        pass