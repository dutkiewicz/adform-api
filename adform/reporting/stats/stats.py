from ...base import Base


class Stats(Base):
    endpoint = 'https://api.adform.com/v1/reportingstats/agency/reportdata'
    body = {
        'dimensions': [],
        'metrics': [],
        'filter': {}
    }

    def dimensions(self, *args):
        self.body['dimensions'] = args
        return self

    def metrics(self, *args):
        self.body['metrics'] = args
        return self

    def filter(self, **kwargs):
        self.body['filter'] = kwargs
        return self

    def exec(self):
        return self._post()
