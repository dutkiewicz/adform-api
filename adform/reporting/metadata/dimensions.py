from ...base import Base


class Dimensions(Base):
    endpoint = 'https://api.adform.com/v1/reportingstats/agency/metadata/dimensions'

    def dimensions(self, *args):
        self.body = {'dimensions': args}
        return self

    def exec(self):
        return self._post()
