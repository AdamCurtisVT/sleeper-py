import requests
import json

class User():
    """
        Calls the Sleeper API for user information.
    """

    @classmethod
    def get_user(self, user_id):
        """
            This endpoint retrieves a specific user.
            Keep in mind that the username of a user can change over time, so if you are storing information, you'll want to hold onto the user_id.
        """
        endpoint = 'https://api.sleeper.app/v1/user/{}'.format(user_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            return response.json()
        else:
            return None
