import credentials
from venmo_api import Client

# You need to import a credentials file with a username, password, and access token
if not credentials.access_token:
    credentials.access_token = Client.get_access_token(
        username=credentials.userName, password=credentials.password)

# initialize venmo client with auth
venmo = Client(access_token=credentials.access_token)
