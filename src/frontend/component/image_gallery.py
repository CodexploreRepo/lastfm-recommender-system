import pandas as pd
import streamlit as st
from src import config
from itertools import cycle


def image_grid():
    # # Visualize aritst
    # print(config.ARTIST_IMAGE_PATH)
    artist_list = ['MALICE MIZER', 'Diary of Dreams', 'Carpathian Forest', 'Moi dix Mois', 'Bella Morte', 'Moonspell']
    num_artist = st.slider("Select Number of Artists for Recommendation", min_value=2, max_value=len(artist_list))
    
    artist_list = artist_list[:num_artist]
    image_path_df = pd.read_csv(config.ARTIST_IMAGE_PATH)
    image_path = image_path_df[image_path_df["artist_name"].apply(lambda x: x in artist_list)]["image_path"].values
   
    cols = cycle(st.columns(len(artist_list))) # st.columns here since it is out of beta at the time I'm writing this
    for idx, filteredImage in enumerate(image_path):
        next(cols).image(filteredImage, use_column_width=True, caption=artist_list[idx].title())
        
   
    
    # with st.container():
    #     for idx, col in enumerate(st.columns(3)):
            
    #         col.image(image_path[idx], width=150, height=100, caption=artist_list[idx])

