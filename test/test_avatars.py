import unittest
from sleeperpy import Avatars

class TestAvatars(unittest.TestCase):

    def test_get_full_size_avatar(capsys):
        avatar = Avatars.get_full_size_avatar('ac3a181698d50b59326b9d0c9c83e9b3')
        assert avatar is not None

    def test_get_thumbnail_avatar(capsys):
        avatar = Avatars.get_thumbnail_avatar('ac3a181698d50b59326b9d0c9c83e9b3')
        assert avatar is not None

if __name__ == '__main__':
    unittest.main()
