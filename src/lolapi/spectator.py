from .api import *


class Match(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'spectator')

    def active_game(self, summoner_id):
        return self.get('active-games', f'by-summoner/{summoner_id}')

    def featured_games(self):
        return self.get('featured-games')
