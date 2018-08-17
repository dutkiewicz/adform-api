from ...base import Base


class Metrics(Base):
    endpoint = '/v1/reportingstats/agency/metadata/metrics'
    body = {
        'metrics': []
    }

    def metrics(self, *args):
        self.body['metrics'] = args
        return self

    def exec(self):
        return self._post()
