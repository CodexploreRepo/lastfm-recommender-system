import pandas as pd
import streamlit as st
from src import config
from src.utils import song_scraper
from itertools import cycle
from src.utils.util import get_recommend_by_user_id, get_user_index
from PIL import Image

# user_id as index
def image_grid(user_name, num_artist, model):
    # # Visualize aritst
    # print(config.ARTIST_IMAGE_PATH)
    st.write(f"### Recommendation by {model}")
    user_id = get_user_index(user_name)
    artist_list = get_recommend_by_user_id(user_id, model)
    # print(artist_list)

    artist_list_new = artist_list[:num_artist]
    # print(artist_list_new)
    image_path_df = pd.read_csv(config.ARTIST_IMAGE_PATH, sep="\t")
    image_path = []
    for name in artist_list_new:
        print(name)
        path = image_path_df[image_path_df.artist_name == name].image_path.values[0]
        image_path.append(path)
    print(image_path)
    cols = st.columns(len(artist_list_new)) # st.columns here since it is out of beta at the time I'm writing this
    for idx, filteredImage in enumerate(image_path):
        print(idx)
        artist_name = artist_list_new[idx]
        cols[idx].image(filteredImage, use_column_width=True, caption=artist_list_new[idx].title())
        tracks = song_scraper.get_top_track_by_artist(artist_name)
        if 'Error' in tracks:
            cols[idx].write("Can't fetch any song")
        else:
            for tr in tracks:
                url = tr['url']
                cols[idx].markdown(f"[{tr['name']}](%s)" % url)
    
    # with st.container():
    #     for idx, col in enumerate(st.columns(3)):
            
    #         col.image(image_path[idx], width=150, height=100, caption=artist_list[idx])

