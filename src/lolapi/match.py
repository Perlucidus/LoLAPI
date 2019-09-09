from .api import *


class Match(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'match')

    def match(self, match_id):
        return self.get('matches', f'{match_id}')

    def by_account(self, account, **kwargs):
        url = f'by-account/{account}'
        if kwargs:
            url += '?'
            params = []
            for k, v in kwargs.items():
                if k in ('champion', 'queue', 'season'):
                    for sv in v:
                        params.append(f'{k}={sv}')
                else:
                    params.append(f'{k}={v}')
            url += '&'.join(params)
        return self.get('matchlists', url)

    def match_timeline(self, match_id):
        return self.get('timelines', f'by-match/{match_id}')

    def tournament_matches(self, tournament_code):
        return self.get('matches', f'by-tournament-code/{tournament_code}/ids')

    def by_tournament_code(self, match_id, tournament_code):
        return self.get('matches', f'{match_id}/by-tournament-code/{tournament_code}')
