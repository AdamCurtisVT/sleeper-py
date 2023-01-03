import unittest
from sleeperpy import User

class TestUser(unittest.TestCase):

    def test_get_user(capsys):
        user_id = '198498154943881216'
        user = User.get_user(user_id)
        assert user is not None

if __name__ == '__main__':
    unittest.main()
