from .api import *


class Status(API):
    def __init__(self, region: str):
        super().__init__(region, 3, 'status')

    def shard_data(self) -> str:
        return self.get('shard-data')
