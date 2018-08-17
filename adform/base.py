from urllib.parse import urljoin

import requests


class Base:
    """Base class for requesting API with ticket"""
    base_url = "https://api.adform.com"
    endpoint = None
    _ticket = None
    body = None
    _headers = {'Authorization': 'Bearer {}'.format(_ticket)}

    def __init__(self, ticket):
        self._ticket = ticket
        self._headers['Authorization'] = 'Bearer {}'.format(self._ticket)
        self.request_url = urljoin(self.base_url, self.endpoint)

    def _get(self, *args):
        if args:
            self.request_url = urljoin(self.request_url, args)

        return requests.get(self.request_url, headers=self._headers).json()

    def _post(self):
        return requests.post(self.request_url, headers=self._headers, json=self.body).json()
