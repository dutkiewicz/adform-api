import requests


class Base:
    """Base class for requesting API with ticket"""
    endpoint = None
    _ticket = None
    body = None
    _headers = {'Authorization': 'Bearer {}'.format(_ticket)}

    def __init__(self, ticket):
        self._ticket = ticket
        self._headers['Authorization'] = 'Bearer {}'.format(self._ticket)

    def _get(self):
        return requests.get(self.endpoint, headers=self._headers).json()

    def _post(self):
        return requests.post(self.endpoint, headers=self._headers, json=self.body).json()
