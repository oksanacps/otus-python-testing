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
        assert len(response['message']) == 98    # Правильно ли сравнивать с числом или лучше список иметь?

    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
        ('australian', 'shepherd'),
        ('bulldog', 'english')
    ])
    def test_random_subbreed_image(self, breed, subbreed):
        request = BaseRequest(BASE_URL_DOG_CEO)
        endpoint = f'breed/{breed}/{subbreed}/images/random'
        response = request.get(endpoint)

        assert response['status'] == 'success'
        assert breed in response['message'] and subbreed in response['message']

    @pytest.mark.parametrize('imgs_number', [1, 3, 5])
    def test_random_images(self, imgs_number):
        request = BaseRequest(BASE_URL_DOG_CEO)
        endpoint = f'breeds/image/random/{imgs_number}'
        response = request.get(endpoint)

        assert response['status'] == 'success'
        assert len(response['message']) == imgs_number

    @pytest.mark.parametrize('breed', ['african', 'boxer', 'chow'])
    def test_random_breed_image(self, breed):
        request = BaseRequest(BASE_URL_DOG_CEO)
        edpoint = f'breed/{breed}/images/random'
        response = request.get(edpoint)

        assert response['status'] == 'success'
        assert breed in response['message']

    @pytest.mark.parametrize('imgs_number, breed', [(1, 'borzoi'), (3, 'briard'), (5, 'clumber')])
    def test_random_breed_images(self, imgs_number, breed):
        request = BaseRequest(BASE_URL_DOG_CEO)
        endpoint = f'breed/{breed}/images/random/{imgs_number}'
        response = request.get(endpoint)

        assert response['status'] == 'success'
        assert len(response['message']) == imgs_number
        for dog in response['message']:
            assert breed in dog

