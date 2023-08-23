import requests


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # headers and etc

    def _request(self, url, request_type, data=None):
        if request_type == 'GET':
            response = requests.get(url)
        elif request_type == 'POST':
            response = requests.post(url, data=data)
        elif request_type == 'FETCH':
            response = requests.post(url, data=data)
        else:
            response = requests.delete(url)

        # log part
        print('*************')
        print(f'{request_type}')
        print(response.url)
        print(response.status_code)
        print(response.reason)
        print(response.text)
        print(response.json())
        print('*************')
        return response

    def get(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'GET')
        return response.json()

    def post(self, endpoint, body):
        url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'POST', data=body)
        return response.json()['message']

    def delete(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'DELETE')
        return response.json()['message']


    def fetch(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'FETCH')
        return response.json()['message']
