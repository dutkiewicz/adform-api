import requests

from adform.exceptions import AuthorizeError


class Authorize:

    endpoint = 'https://id.adform.com/sts/connect/token'
    access_token = None
    expires_in = None

    def __init__(self, client_id, client_secret, *scopes):
        self.body = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials',
            'scope': scopes
        }

        self._authorize()

    def _authorize(self):
        response = requests.post(self.endpoint, data=self.body)

        if response.status_code != 200:
            msg = response.json()
            raise AuthorizeError(
                "Error HTTP {}! Can't authorize credentials, reason: {}".format(response.status_code, msg['error']))

        response = response.json()
        self.access_token = response['access_token']
        self.expires_in = response['expires_in']
        return self.access_token

    def __repr__(self):
        return self.access_token
