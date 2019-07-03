#-------------------------------------------------
# Imports
#-------------------------------------------------
import json
import requests
import sys

#-------------------------------------------------
# Classes
#-------------------------------------------------

# Represents a Sleeper.app Avatar.
class Avatar(object):
    Avatar = None

    # Initializes a new instance of the Avatar class.
    def __init__(self, content):
        self.Avatar = content

#-------------------------------------------------
# Functions
#-------------------------------------------------

# Call the Sleeper API to retrieve a full size avatar.
def GetFullSizeAvatar(avatarId):
    if not avatarId:
        raise ValueError('The Avatar ID must not be null.') 
    endpoint = ('https://sleepercdn.com/avatars/{}'.format(avatarId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        return Avatar(response.content)
    else:
        return None

# Call the Sleeper API to retrieve a thumbnail avatar.
def GetThumbnailAvatar(avatarId):
    if not avatarId:
        raise ValueError('The Avatar ID must not be null.') 
    endpoint = ('https://sleepercdn.com/avatars/thumbs/{}'.format(avatarId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        return Avatar(response.content)
    else:
        return None
        