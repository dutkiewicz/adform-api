import configparser
import unittest

import adform


class AuthorizeTestCase(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.client_id = config['DEFAULT']['CLIENT_ID']
        self.client_secret = config['DEFAULT']['CLIENT_SECRET']

    def test_token_repr_is_str(self):
        token = adform.auth.Authorize(self.client_id, self.client_secret)
        self.assertIsInstance(repr(token), str)

    def test_raise_auth_exception(self):
        with self.assertRaises(adform.exceptions.AuthorizeError):
            self.client_id += 'XXX'
            adform.auth.Authorize(self.client_id, self.client_secret)


if __name__ == '__main__':
    unittest.main()
