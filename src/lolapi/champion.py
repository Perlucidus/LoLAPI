from api import *


class Champion(API):
    def __init__(self, region: str):
        super().__init__(region, 3, 'platform')

    def rotations(self) -> str:
        return self.get('champion-rotations')
