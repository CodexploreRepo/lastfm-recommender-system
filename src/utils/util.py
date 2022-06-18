

from src import config
import pandas as pd
from os import path

def get_recomendation(file):
    users = []
    with open(file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            artists = line.split(" ")
            artists = [int(idx) for idx in artists]
            users.append(artists)
    return users

def get_recommend_by_user_id(idx, model):
    idx = int(idx)
    print(idx)
    print(config.RESULT)
    model_result_file = path.join(config.RESULT, f"{model}.txt")
    users = get_recomendation(model_result_file)
    artist = pd.read_csv(config.ARTIST_DAT, sep='\t')
    artist.name = artist.name.apply(lambda x: str(x))
    # artist_name = artist.artist_name[users[0]]
    artist_name = []
    for i in users[idx]:
        name = artist[artist.id == i]['name'].values[0]
        artist_name.append(name)
    # print(artist_name.to_list())
    return artist_name


def name_generation(num_name):
    names = []
    with open(config.NAMES, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            names.append(line.strip())
    return names[:num_name]