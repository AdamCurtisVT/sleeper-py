import unittest
from sleeperpy import Leagues

class TestLeagues(unittest.TestCase):

    def test_get_all_leagues(capsys):
        user_id = '198498154943881216'
        sport = 'nfl'
        season = 2022
        leagues = Leagues.get_all_leagues(user_id, sport, season)
        assert leagues is not None

    def test_get_league(capsys):
        league_id = '846566237667467264'
        league = Leagues.get_league(league_id)
        assert league is not None

    def test_get_rosters(capsys):
        league_id = '846566237667467264'
        rosters = Leagues.get_rosters(league_id)
        assert rosters is not None

    def test_get_users(capsys):
        league_id = '846566237667467264'
        users = Leagues.get_users(league_id)
        assert users is not None

    def test_get_matchups(capsys):
        league_id = '846566237667467264'
        week = 1
        matchups = Leagues.get_matchups(league_id, week)
        assert matchups is not None

    def test_get_winners_playoff_bracket(capsys):
        league_id = '846566237667467264'
        matchups = Leagues.get_winners_playoff_bracket(league_id)
        assert matchups is not None

    def test_get_losers_playoff_bracket(capsys):
        league_id = '846566237667467264'
        matchups = Leagues.get_losers_playoff_bracket(league_id)
        assert matchups is not None

    def test_get_transactions(capsys):
        league_id = '846566237667467264'
        round = 1
        transactions = Leagues.get_transactions(league_id, round)
        assert transactions is not None

    def test_get_traded_picks(capsys):
        league_id = '846566237667467264'
        picks = Leagues.get_traded_picks(league_id)
        assert picks is not None

    def get_state(capsys):
        sport = 'nfl'
        state = Leagues.get_state(sport)
        assert state is not None
