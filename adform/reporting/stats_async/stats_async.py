import datetime
from urllib.parse import urljoin

import requests

from ...base import Base


class StatsAsync(Base):
    endpoint = "/v1/buyer/stats/data"
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
        if not isinstance(start, datetime.datetime):
            raise TypeError("Start date must be datetime object!")
        if not isinstance(end, datetime.datetime):
            raise TypeError("End date must be datetime object!")

        self.body["filter"]["date"]["to"] = end.isoformat()
        self.body["filter"]["date"]["from"] = start.isoformat()

        return self

    def create(self):
        if not self.body["filter"]["date"]["from"]:
            raise ValueError("Report start time must be specified!")
        if not self.body["filter"]["date"]["to"]:
            raise ValueError("Report end time must be specified!")

        response = requests.post(self.request_url, headers=self._headers, json=self.body)

        if response.status_code == 202:
            return response.headers
        else:
            raise RuntimeError(response.status_code, response.content)

    def get(self, location):
        url = urljoin(self.base_url, location)
        return requests.get(url, headers=self._headers).json()

    def delete(self, location):
        url = urljoin(self.base_url, location)
        response = requests.delete(url, headers=self._headers)

        if response.status_code == 204:
            return response.status_code
        else:
            raise RuntimeError(response.status_code, response.content)
