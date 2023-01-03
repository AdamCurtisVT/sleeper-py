import unittest
from sleeperpy import Players

class TestPlayers(unittest.TestCase):

    def test_get_all_players(capsys):
        players = Players.get_all_players()
        assert players is not None

    def test_get_trending_players(capsys):
        sport = 'nfl'
        type = 'add'
        hours = 24
        limit = 10
        players = Players.get_trending_players(sport, type, hours, limit)
        assert players is not None

if __name__ == '__main__':
    unittest.main()
