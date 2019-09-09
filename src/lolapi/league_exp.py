from .api import *


class LeagueExp(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'league-exp')

    def entries(self, queue, tier, division, page: int = None):
        params = {}
        if page:
            params = {'page': page}
        return self.get('entries', f'{queue}/{tier}/{division}', params)
