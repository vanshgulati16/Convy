import json
import spotipy

from credentials import my_client_id, my_client_secret
from spotipy.oauth2 import SpotifyClientCredentials

# Creating API
def connect(client_id, client_secret):
    sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=my_client_id, client_secret=my_client_secret
        )
    )
    return sp

# Fetching playlist
def get_playlist_by_id(sp, playlist_id):
    playlist_res = sp.playlist(playlist_id)
    name = playlist_res['name']
    playlist_items = playlist_res['tracks']['items']

    return name, playlist_items

def extract_data(api, items):
    tracks = []
    for i in items:
            items = dict.fromkeys(['track_name', 'artist_name', 'album_name'])
            track_name = i['track']['name']
            artist_name = i['track']['artists'][0]['name']
            album_name = i['track']['album']['name']

            items['track_name'] = track_name
            items['artist_name'] = artist_name
            items['album_name'] = album_name

            tracks.append(items)

    return tracks

# query for yt
def query_builder(pl_data):
     queries = []
     for i in pl_data:
         query = "{}{}{}".format(i['track_name'], i['artist_name'], i['album_name'])
         queries.append(query)
     return queries

# pl_id = '2enQfa7gFxNDWJrKAmllMQ'

# api = connect(my_client_id, my_client_secret)
# playlist_items = get_playlist_by_id(api, pl_id)

# print(json.dumps(playlist_items))

