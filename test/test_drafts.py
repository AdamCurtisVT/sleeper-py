import unittest
from sleeperpy import Drafts

class TestDrafts(unittest.TestCase):

    def test_get_all_drafts_for_user(capsys):
        user_id = '198498154943881216'
        sport = 'nfl'
        season = 2022
        drafts = Drafts.get_all_drafts_for_user(user_id, sport, season)
        assert drafts is not None

    def test_get_all_drafts_for_league(capsys):
        league_id = '846566237667467264'
        drafts = Drafts.get_all_drafts_for_league(league_id)
        assert drafts is not None

    def test_get_specific_draft(capsys):
        draft_id = '846566237667467265'
        drafts = Drafts.get_specific_draft(draft_id)
        assert drafts is not None

    def test_get_all_picks_in_draft(capsys):
        draft_id = '846566237667467265'
        drafts = Drafts.get_all_picks_in_draft(draft_id)
        assert drafts is not None

    def test_get_traded_picks_in_draft(capsys):
        draft_id = '846566237667467265'
        drafts = Drafts.get_traded_picks_in_draft(draft_id)
        assert drafts is not None

if __name__ == '__main__':
    unittest.main()
