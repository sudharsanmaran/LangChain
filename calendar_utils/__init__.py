import json
from os import path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


flow = InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile',
            'https://www.googleapis.com/auth/calendar'])

flow.run_local_server()
credentials = flow.credentials
# with open('token.json', 'w') as token:
#     json.dump(credentials, token)

service = build('calendar', 'v3', credentials=credentials)

