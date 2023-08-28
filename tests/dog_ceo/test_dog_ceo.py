import pytest


@pytest.mark.dog
class TestDogCeo:
    """

    """
    def test_list_all_dogs(self, get_request_instance):
        request = get_request_instance
        response = request.get(endpoint='breeds/list/all')

        assert response['status'] == 'success'
        assert len(response['message']) == 98

    @pytest.mark.parametrize('breed, subbreed', [
        ('hound', 'afghan'),
        ('australian', 'shepherd'),
        ('bulldog', 'english')
    ])
    def test_random_subbreed_image(self, breed, subbreed, get_request_instance):
        request = get_request_instance
        response = request.get(endpoint=f'breed/{breed}/{subbreed}/images/random')

        assert response['status'] == 'success'
        assert breed in response['message'] and subbreed in response['message']

    @pytest.mark.parametrize('imgs_number', [1, 3, 5])
    def test_random_images(self, imgs_number, get_request_instance):
        request = get_request_instance
        response = request.get(endpoint=f'breeds/image/random/{imgs_number}')

        assert response['status'] == 'success'
        assert len(response['message']) == imgs_number

    @pytest.mark.parametrize('breed', ['african', 'boxer', 'chow'])
    def test_random_breed_image(self, breed, get_request_instance):
        request = get_request_instance
        response = request.get(endpoint=f'breed/{breed}/images/random')

        assert response['status'] == 'success'
        assert breed in response['message']

    @pytest.mark.parametrize('imgs_number, breed', [(1, 'borzoi'), (3, 'briard'), (5, 'clumber')])
    def test_random_breed_images(self, imgs_number, breed, get_request_instance):
        request = get_request_instance
        response = request.get(endpoint=f'breed/{breed}/images/random/{imgs_number}')

        assert response['status'] == 'success'
        assert len(response['message']) == imgs_number
        for dog in response['message']:
            assert breed in dog
