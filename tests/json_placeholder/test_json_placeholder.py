import pytest


@pytest.mark.placehplder
class TestJsonPlaceholder:
    """

    """

    def test_json_placeholder1(self):
        # base_request = BaseRequest(test_data.BASE_URL_DOG_CEO)
        # response = base_request.get('example', 1)
        # assert response.ok
        pass


    def test_json_placeholder2(self):
        pass

    def test_json_placeholder3(self):
        pass

    @pytest.mark.parametrize('example', [1, 2])
    def test_json_placeholder4(self, example):
        pass

    @pytest.mark.parametrize('example',[1,2])
    def test_json_placeholder5(self, example):
        pass
