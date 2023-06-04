# import json
import os

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow


# from yt_search import MakePublicService

def makeList():
    credentials = None


# toekn.pickle stores the user's credentials from previously successful logins
    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

# if there are no valid credentials available, then either refresh the token or log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json',
                scopes=[
                    'https://www.googleapis.com/auth/youtube.force-ssl'
                ]
            )

            flow.run_local_server(
                port=8080,
                prompt='consent',
                authorization_prompt_message=''
            )
            credentials = flow.credentials

    print(credentials.to_json())
# saving credentials for future use
    with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)

    youtube = build('youtube', 'v3', credentials=credentials)

    return youtube

def makePlayList(serv, name):
    request = serv.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": str(name),
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
    return response['id']


def addItemToPlayList(serv, playlist_id, video_id,items):
    res = []
    for i in items:
        request = serv.playlistItems().insert(
            part="snippet",
            body={
              "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                  "kind": "youtube#video",
                  "videoId": i
                }
              }
            }
        )
        response = request.execute()
        print('Added')
        res.append(response)

    return res


# flow = InstalledAppFlow.from_client_secrets_file(
#                 'client_secret.json',
#                 scopes=[
#                     'https://www.googleapis.com/auth/youtube.readonly'
#                 ]
#             )

# flow.run_local_server(
#                 port=8080,
#                 prompt='consent',
                
# )
# credentials = flow.credentials

# print(credentials.to_json())