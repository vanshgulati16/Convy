from credentials import yt_api_key, my_client_id, my_client_secret
from spotify_extrator import connect, get_playlist_by_id, extract_data, query_builder
from yt_auth import makeList, makePlayList, addItemToPlayList
from yt_search import get_video_id

playlist_id = "2enQfa7gFxNDWJrKAmllMQ"

def main():
    api = connect(my_client_id, my_client_secret)
    playlist_items = get_playlist_by_id(api, playlist_id)
    pl_name = playlist_items[0]
    # queries = query_builder(extract_data(api, playlist_items[1]))
    ids = get_video_id(yt_api_key)

    service = makeList()
    new_pl_id = makePlayList(service, pl_name)
    addItemToPlayList(service, new_pl_id, ids)

    return new_pl_id


print(main())
