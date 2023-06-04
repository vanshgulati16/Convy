from googleapiclient.discovery import build
from credentials import yt_api_key
# from spotify_extrator import query_builder

import time


def get_video_id(queris):
    global video_id
    youtube = build('youtube', 'v3', developerKey=yt_api_key)
    ids = []
    # for i in range(len(queris)):
    request = youtube.search().list(
    part='snippet',
    maxResults=2,
    q = queris
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    # video_id.append(response['items'][1]['id']['videoId'])
    print(video_id)
    ids.append(video_id)

    time.sleep(2)
    
    return ids

print(get_video_id(queris=['yessirski']))