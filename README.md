# sleeper-py
A python implementation of the Sleeper API. Original documentation for these API calls can be found at https://docs.sleeper.app/.

# Install
~~~
pip install sleeper-py
~~~

# Usage
## Avatars
### get_full_size_avatar()
~~~
from sleeperpy import Avatars
Avatars.get_full_size_avatar(avatar_id)
~~~
### get_thumbnail_avatar()
~~~
from sleeperpy import Avatars
Avatars.get_thumbnail_avatar(avatar_id)
~~~

## Drafts
### get_all_drafts_for_user()
~~~
from sleeperpy import Drafts
Drafts.get_all_drafts_for_user(user_id, sport, season)
~~~
### get_all_drafts_for_league()
~~~
from sleeperpy import Drafts
Drafts.get_all_drafts_for_league(league_id)
~~~
### get_specific_draft()
~~~
from sleeperpy import Drafts
Drafts.get_specific_draft(draft_id)
~~~
### get_all_picks_in_draft()
~~~
from sleeperpy import Drafts
Drafts.get_all_picks_in_draft(draft_id)
~~~
### get_traded_picks_in_draft()
~~~
from sleeperpy import Drafts
Drafts.get_traded_picks_in_draft(draft_id)
~~~

## Leagues
### get_all_leagues()
~~~
from sleeperpy import Leagues
Leagues.get_all_leagues(user_id, sport, season)
~~~
### get_league()
~~~
from sleeperpy import Leagues
Leagues.get_league(league_id)
~~~
### get_rosters()
~~~
from sleeperpy import Leagues
Leagues.get_rosters(league_id)
~~~
### get_users()
~~~
from sleeperpy import Leagues
Leagues.get_users(league_id)
~~~
### get_matchups()
~~~
from sleeperpy import Leagues
Leagues.get_matchups(league_id, week)
~~~
### get_winners_playoff_bracket()
~~~
from sleeperpy import Leagues
Leagues.get_winners_playoff_bracket(league_id)
~~~
### get_losers_playoff_bracket()
~~~
from sleeperpy import Leagues
Leagues.get_losers_playoff_bracket(league_id)
~~~
### get_transactions()
~~~
from sleeperpy import Leagues
Leagues.get_transactions(league_id, round)
~~~
### get_traded_picks()
~~~
from sleeperpy import Leagues
Leagues.get_traded_picks(league_id)
~~~
### get_state()
~~~
from sleeperpy import Leagues
Leagues.get_state(sport)
~~~

## Players
### get_all_players()
~~~
from sleeperpy import Players
Players.get_all_players()
~~~
### get_trending_players()
~~~
from sleeperpy import Players
Players.get_trending_players(sport, type, hours, limit)
~~~

## User
### get_user()
~~~
from sleeperpy import User
User.get_user(user_id)
~~~

# Example
This example shows how to retrieve a user ID and use it to query for leagues and matchups for week 1 of the 2022 NFL season.
~~~
account = User.get_user('account_name')
sport = 'nfl'
season = 2022
week = 1

leagues = Leagues.get_all_leagues(account['user_id'], sport, season)
for league in leagues:
    league_id = league['league_id']
    matchups = Leagues.get_matchups(league_id, week)
~~~
