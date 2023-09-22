# import os
# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build

# from googleapiclient.errors import HttpError


# from google_auth_oauthlib.flow import InstalledAppFlow


# flow = InstalledAppFlow.from_client_secrets_file(
#     'client_secrets.json',
#     scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'])

# def get_google_calendar_service():
#     SCOPES = ['https://www.googleapis.com/auth/calendar']
#     creds = None

#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#     try:
#         service = build('calendar', 'v3', credentials=creds)
#         return service
#     except HttpError as error:
#         print('An error occurred while initializing Google Calendar service: %s' % error)
#         return None



# if __name__ == '__main__':
#     calendar_service = get_google_calendar_service()

