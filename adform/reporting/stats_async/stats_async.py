import datetime

from adform.base import Base


class StatsAsync(Base):
    body = {
        "dimensions": [],
        "metrics": [],
        "filter": {
            "date": {
                "from": None,
                "to": None
            }
        }
    }

    def dimensions(self, *args):
        self.body["dimensions"] = list(args)
        return self

    def metrics(self, *args):
        self.body["metrics"] = list(args)
        return self

    def filter(self, **kwargs):
        self.body["filter"].update(kwargs)
        return self

    def daterange(self, start, end):
        """Accepts datetime objects or string formatted YYYY-MM-DD"""
        if isinstance(start, datetime.datetime):
            pass
        elif isinstance(start, str):
            start = datetime.datetime.strptime(start, '%Y-%M-%d')
        else:
            raise TypeError("Start date must be datetime object or string formatted YYYY-MM-DD!")

        if isinstance(end, datetime.datetime):
            pass
        elif isinstance(end, str):
            end = datetime.datetime.strptime(end, '%Y-%M-%d')
        else:
            raise TypeError("End date must be datetime object or string formatted YYYY-MM-DD!")

        self.body["filter"]["date"]["to"] = end.isoformat()
        self.body["filter"]["date"]["from"] = start.isoformat()

        return self

    def create_data(self):
        if not self.body["filter"]["date"]["from"]:
            raise ValueError("Report start time must be specified!")
        if not self.body["filter"]["date"]["to"]:
            raise ValueError("Report end time must be specified!")

        endpoint = '/v1/buyer/stats/data'
        response = self._post(endpoint)

        self.operation_location = response.headers['operation-location']
        self.location = response.headers['location']
        return self

    def get_data(self, id=None):
        endpoint = '/v1/buyer/data/{}'.format(id) if id else self.location
        return self._get(endpoint).json()

    def delete_data(self, id=None):
        endpoint = '/v1/buyer/data/{}'.format(id) if id else self.location
        return self._delete(endpoint)

    def get_operation(self, id=None):
        endpoint = '/v1/buyer/operations/{}'.format(id) if id else self.operation_location
        return self._get(endpoint).json()

    def delete_operation(self, id=None):
        endpoint = '/v1/buyer/operations/{}'.format(id) if id else self.operation_location
        return self._delete(endpoint)
