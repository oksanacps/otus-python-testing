import pytest


@pytest.mark.placehplder
class TestJsonPlaceholder:
    """

    """

    def test_get_all_posts(self, get_request_instance):
        base_request = get_request_instance
        _id = 1
        response = base_request.get(endpoint='posts')
        assert len(response) == 100
        for post in response:
            assert post['id'] == _id
            _id += 1

    @pytest.mark.parametrize('_id, expected_len', [(1, 4), (55, 4), (100, 4), (0, 0), (101, 0)])
    def test_get_post_by_id(self, _id, expected_len, get_request_instance):
        base_request = get_request_instance
        response = base_request.get(endpoint='posts', endpoint_id=_id)
        assert len(response) == expected_len
        if 0 < _id <= 100:
            assert response['id'] == _id

    @pytest.mark.parametrize('post_id', [1, 2, 3])
    def test_get_post_by_postid_endpoint(self, post_id, get_request_instance):
        base_request = get_request_instance
        response = base_request.get(endpoint=f'posts/{post_id}/comments')
        for post in response:
            assert post['postId'] == post_id

    @pytest.mark.parametrize('post_id', [1, 2, 3])
    def test_get_post_by_postid_parameter(self, post_id, get_request_instance):
        base_request = get_request_instance
        response = base_request.get(endpoint='/comments', params={'postId': post_id})
        for post in response:
            assert post['postId'] == post_id

    def test_create_post(self, get_request_instance):
        base_request = get_request_instance
        body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = base_request.post(endpoint='posts', body=body)
        assert response['id']
        assert response['title'] == 'foo'

    def test_update_post(self, get_post_by_id):
        old_title, _id, base_request = get_post_by_id
        body = {
            'id': int(_id),
            'title': 'foo_temp',
            'body': 'bar',
            'userId': 1,
        }
        response = base_request.put(endpoint='posts', endpoint_id=1, body=body)
        assert response['title'] == 'foo_temp'
        assert response['title'] != old_title
