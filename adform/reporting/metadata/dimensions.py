from ...base import Base


class Dimensions(Base):
    endpoint = '/v1/reportingstats/agency/metadata/dimensions'
    body = {
        'dimensions': []
    }

    def dimensions(self, *args):
        self.body['dimensions'] = args
        return self

    def exec(self):
        return self._post()
