# LoLAPI
League of Legends API Library

## Usage Example
```
import api_manager
from summoner import Summoner

api_manager.initialize('YOUR API KEY HERE')
summoner = Summoner('eun1')
october = summoner.by_name('October')
print(october['summonerLevel'])
print(api_manager.api_request_rate(120))
```

## [License](LICENSE)

LolAPI isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games
or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are
trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
