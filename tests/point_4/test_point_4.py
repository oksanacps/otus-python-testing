import pytest
import requests


@pytest.mark.test
def test_status_code(url, status_code):
    response = requests.get(url=url)
    assert response.status_code == int(status_code)
