import requests
from src import config


def get_top_track_by_geo(country):

        headers = {
        'user-agent': config.USER_AGENT
        }

        payload = {
        'api_key': config.API_KEY,
        'method': 'geo.gettopartists',
        'country': country,
        'limit': config.LIMIT_TOP_SONG,
        'format': 'json'
        }

        r = requests.get(config.BASE_URL, headers=headers, params=payload) 
        if r.status_code == 200:
            return r.json()['topartists']['artist']
        return {'Error': 'Fetching tracks error'}
# print(get_top_track_by_geo("Singapore"))

def get_top_track_by_artist(artist_name):    

    headers = {
    'user-agent': config.USER_AGENT
    }

    payload = {
    'api_key': config.API_KEY,
    'method': 'artist.gettoptracks',
    'artist': artist_name,
    'limit': config.LIMIT_TOP_SONG,
    'format': 'json'
    }

    r = requests.get(config.BASE_URL, headers=headers, params=payload) 
    if r.status_code == 200:
        return r.json()['toptracks']['track']
    return {'Error': 'Fetching tracks error'}