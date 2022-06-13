import requests
from src import config


def get_top_track_by_artist(artist_id):
    pass


def get_top_track_by_artist(artist_name):    
    limit=5
    headers = {
    'user-agent': config.USER_AGENT
    }

    payload = {
    'api_key': config.API_KEY,
    'method': 'artist.gettoptracks',
    'artist': artist_name,
    'limit': limit,
    'format': 'json'
    }

    r = requests.get(config.BASE_URL, headers=headers, params=payload) 
    if r.status_code == 200:
        return r.json()['toptracks']['track']
    return {'Error': 'Fetching tracks error'}