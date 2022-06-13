import pandas as pd
import streamlit as st
from src import config
from src.utils import song_scraper
from itertools import cycle


def image_grid():
    # # Visualize aritst
    # print(config.ARTIST_IMAGE_PATH)
    artist_list = ['MALICE MIZER', 'Diary of Dreams', 'Carpathian Forest', 'Moi dix Mois', 'Bella Morte', 'Moonspell']
    num_artist = st.slider("Select Number of Artists for Recommendation", min_value=2, max_value=len(artist_list))
    
    artist_list = artist_list[:num_artist]
    image_path_df = pd.read_csv(config.ARTIST_IMAGE_PATH)
    image_path = image_path_df[image_path_df["artist_name"].apply(lambda x: x in artist_list)]["image_path"].values
   
    cols = st.columns(len(artist_list)) # st.columns here since it is out of beta at the time I'm writing this
    for idx, filteredImage in enumerate(image_path):
        print(idx)
        artist_name = artist_list[idx]
        cols[idx].image(filteredImage, use_column_width=True, caption=artist_list[idx].title())
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

