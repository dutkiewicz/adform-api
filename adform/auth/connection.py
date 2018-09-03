import requests


class Connection:
    """
    TODO zrobić strategię buildera
    """

    endpoint = 'https://id.adform.com/sts/connect/token'
    access_token = None
    expires_in = None

    def __init__(self, client_id, client_secret, *scope):
        self.scope = scope
        self.body = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials',
            'scope': self.scope
        }
        self.authorize()

    def authorize(self):
        response = requests.post(self.endpoint, data=self.body).json()
        self.access_token = response['access_token']
        self.expires_in = response['expires_in']
        return self.access_token

    def __repr__(self):
        return self.access_token
