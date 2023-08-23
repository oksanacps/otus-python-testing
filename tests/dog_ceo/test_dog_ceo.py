import pytest

from test_data.url_data import BASE_URL_DOG_CEO
from src.base_request import BaseRequest


@pytest.mark.dog
class TestDogCeo:
    """

    """
    @pytest.mark.test
    def test_list_all_dogs(self):
        request = BaseRequest(BASE_URL_DOG_CEO)
        response = request.get('breeds/list/all')
        
        assert response['status'] == 'success'
        assert len(response['message']) == 98


    def test_dog_ceo2(self):
        pass

    def test_dog_ceo3(self):
        pass

    @pytest.mark.parametrize('example', [1, 2])
    def test_dog_ceo4(self, example):
        pass

    @pytest.mark.parametrize('example', [1, 2])
    def test_dog_ceo5(self, example):
        pass
