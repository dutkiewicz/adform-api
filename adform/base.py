from urllib.parse import urljoin

import requests

from adform import exceptions


class Base:
    """Base class for requesting API with ticket. Containst common http methods like GET, POST, PUT, DELETE."""
    base_url = "https://api.adform.com"
    _ticket = None
    body = None
    _headers = {'Authorization': 'Bearer {}'.format(_ticket)}

    def __init__(self, ticket):
        self._ticket = ticket
        self._headers['Authorization'] = 'Bearer {}'.format(self._ticket)

    def _get(self, endpoint):
        url = urljoin(self.base_url, endpoint)
        response = requests.get(url, headers=self._headers)

        if response.status_code >= 200 or response.status_code < 300:
            return response
        elif response.status_code == 400:
            error_msg = response.json()
            raise exceptions.BadRequestError("Error {}. Reason: {}".format(response.status_code,
                                                                           error_msg['reason']))
        elif response.status_code == 401:
            error_msg = response.json()
            raise exceptions.UnauthorizedError("Error {}. Reason: {}".format(response.status_code,
                                                                             error_msg['reason']))
        elif response.status_code == 403:
            error_msg = response.json()
            raise exceptions.ForbiddenError("Error {}. Reason: {}".format(response.status_code,
                                                                          error_msg['reason']))
        elif response.status_code == 429:
            error_msg = response.json()
            raise exceptions.QuotaLimitExceededError("Error {}. Reason: {}".format(response.status_code,
                                                                                   error_msg['reason']))
        else:
            raise exceptions.ApiError('There was an ambiguous error while processing your request.')

    def _post(self, endpoint):
        url = urljoin(self.base_url, endpoint)
        response = requests.post(url, headers=self._headers, json=self.body)

        if response.status_code >= 200 or response.status_code < 300:
            return response
        elif response.status_code == 400:
            error_msg = response.json()
            raise exceptions.BadRequestError("Error {}. Reason: {}".format(response.status_code,
                                                                           error_msg['reason']))
        elif response.status_code == 401:
            error_msg = response.json()
            raise exceptions.UnauthorizedError("Error {}. Reason: {}".format(response.status_code,
                                                                             error_msg['reason']))
        elif response.status_code == 403:
            error_msg = response.json()
            raise exceptions.ForbiddenError("Error {}. Reason: {}".format(response.status_code,
                                                                          error_msg['reason']))
        elif response.status_code == 429:
            error_msg = response.json()
            raise exceptions.QuotaLimitExceededError("Error {}. Reason: {}".format(response.status_code,
                                                                                   error_msg['reason']))
        else:
            raise exceptions.ApiError('There was an ambiguous error while processing your request.')

    def _put(self, endpoint):
        url = urljoin(self.base_url, endpoint)
        response = requests.post(url, headers=self._headers, json=self.body)

        if response.status_code >= 200 or response.status_code < 300:
            return response
        elif response.status_code == 400:
            error_msg = response.json()
            raise exceptions.BadRequestError("Error {}. Reason: {}".format(response.status_code,
                                                                           error_msg['reason']))
        elif response.status_code == 401:
            error_msg = response.json()
            raise exceptions.UnauthorizedError("Error {}. Reason: {}".format(response.status_code,
                                                                             error_msg['reason']))
        elif response.status_code == 403:
            error_msg = response.json()
            raise exceptions.ForbiddenError("Error {}. Reason: {}".format(response.status_code,
                                                                          error_msg['reason']))
        elif response.status_code == 429:
            error_msg = response.json()
            raise exceptions.QuotaLimitExceededError("Error {}. Reason: {}".format(response.status_code,
                                                                                   error_msg['reason']))
        else:
            raise exceptions.ApiError('There was an ambiguous error while processing your request.')

    def _delete(self, endpoint):
        url = urljoin(self.base_url, endpoint)
        response = requests.delete(url, headers=self._headers)

        if response.status_code >= 200 or response.status_code < 300:
            return response
        elif response.status_code == 400:
            error_msg = response.json()
            raise exceptions.BadRequestError("Error {}. Reason: {}".format(response.status_code,
                                                                           error_msg['reason']))
        elif response.status_code == 401:
            error_msg = response.json()
            raise exceptions.UnauthorizedError("Error {}. Reason: {}".format(response.status_code,
                                                                             error_msg['reason']))
        elif response.status_code == 403:
            error_msg = response.json()
            raise exceptions.ForbiddenError("Error {}. Reason: {}".format(response.status_code,
                                                                          error_msg['reason']))
        elif response.status_code == 429:
            error_msg = response.json()
            raise exceptions.QuotaLimitExceededError("Error {}. Reason: {}".format(response.status_code,
                                                                                   error_msg['reason']))
        else:
            raise exceptions.ApiError('There was an ambiguous error while processing your request.')
