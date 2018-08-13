from boxsdk import Client
from boxsdk import OAuth2

from BOX_MAN import config_oauth

# Create new OAuth client & csrf token
oauth = OAuth2(
  client_id=config_oauth.client_id,
  client_secret=config_oauth.client_secret
)
#csrf_token = ''

auth_url, csrf_token = oauth.get_authorization_url(config_oauth.redirect_uri)

file_path ='C:\\Users\Victor\Documents\language.txt'
file_name = 'language.txt'
folder_id = 'yeet'

client = Client(oauth)

box_file = client.folder(folder_id).upload(file_path, file_name)

#transition.txt
