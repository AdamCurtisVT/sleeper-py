#-------------------------------------------------
# Imports
#-------------------------------------------------
import json
import requests
import sys

#-------------------------------------------------
# Classes
#-------------------------------------------------

# Represents a Sleeper.app user.
class User(object):
    AvatarId = None
    Cookies = None
    Created = None
    Currencies = None
    DataUpdated = None
    Deleted = None
    DisplayName = None
    Email = None
    IsBot = False
    Notifications = None
    Pending = None
    Phone = None
    RealName = None
    Solicitable = None
    Token = None
    UserId = None
    Username = None
    Verification = None

    # Initializes a new instance of the User class.
    def __init__(self, jsonText):
        self.AvatarId = jsonText['avatar']
        self.Cookies = jsonText['cookies']
        self.Created = jsonText['created']
        self.Currencies = jsonText['currencies']
        self.DataUpdated = jsonText['data_updated']
        self.Deleted = jsonText['deleted']
        self.DisplayName = jsonText['display_name']
        self.Email = jsonText['email']
        self.IsBot = jsonText['is_bot']
        self.Notifications = jsonText['notifications']
        self.Pending = jsonText['pending']
        self.Phone = jsonText['phone']
        self.RealName = jsonText['real_name']
        self.Solicitable = jsonText['solicitable']
        self.Token = jsonText['token']
        self.UserId = jsonText['user_id']
        self.Username = jsonText['username']
        self.Verification = jsonText['verification']

#-------------------------------------------------
# Functions
#-------------------------------------------------

# Call the Sleeper API to retrieve a user.
def GetUser(userId):
    if not userId:
        raise ValueError('The User ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/user/{}'.format(userId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        return User(responseJson)
    else:
        return None
        