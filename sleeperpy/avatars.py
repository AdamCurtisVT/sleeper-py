import requests

class Avatars():
    """
        Calls the Sleeper API for avatar information.
    """
    
    @classmethod
    def get_full_size_avatar(self, avatar_id):
        """
            Users and leagues have avatar images. This endpoint retrieves the full size avatar.
        """
        endpoint = 'https://sleepercdn.com/avatars/{}'.format(avatar_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            return response.content
        else:
            return None

    @classmethod
    def get_thumbnail_avatar(self, avatar_id):
        """
            Users and leagues have avatar images. This endpoint retrieves the thumbnail avatar.
        """
        endpoint = 'https://sleepercdn.com/avatars/thumbs/{}'.format(avatar_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            return response.content
        else:
            return None
