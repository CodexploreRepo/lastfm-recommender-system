import streamlit as st
from src import config
from src.frontend.component.image_gallery import image_grid
from src.frontend.component import display_logo
from src.utils import song_scraper
from src.utils.util import name_generation, get_friend_list
import pandas as pd



import datetime
hour = datetime.datetime.now().hour

greeting = "Good Morning" if 5<=hour<12 else "Good Afternoon" if 12<=hour<18 else "Good Evening"

# Set up webframe
st.set_page_config(page_title=config.PAGE_TITLE, layout="wide", initial_sidebar_state="auto")


# List of recommendation
user_list = name_generation(config.NUM_OF_USERS)
models =["MostPop",  "WMF", "SoRec", "BPR", "VAECF", "CTR", "Ensemble"]

display_logo()

index = st.sidebar.selectbox("User List", range(len(user_list)), format_func=lambda x: user_list[x])
model_list = st.sidebar.multiselect("Model Selection", models, default= "WMF")


user_name = user_list[index]
# st.write("index:", index)


st.write(f"# {config.TITLE}")
st.write(f"""
    ### {greeting}, {user_name} ! 
    #### Personalized Music Recommendation
""")
num_artist = st.slider("Select Number of Artists for Recommendation", min_value=5, max_value=15)
for model in model_list:
    st.write(f"#### Suggestions from {model} Model")
    image_grid(user_name, num_artist, model)

    if model == 'SoRec':
        friends = get_friend_list(user_name)
        friend = st.sidebar.selectbox("Friend List",friends)
        st.write(f"### Recommend for your friend, {friend}")
        image_grid(friend, num_artist, model)

# get top artist
st.write(f"### Most Popular Artist NOW in {config.COUNTRY}")
top_artist = song_scraper.get_top_artist_by_geo("Singapore")
if 'Error' in top_artist:
    st.write("Can't fetch any artists")
else:
    for tr in top_artist:
        url = tr['url']
        st.markdown(f"[{tr['name']}](%s)" % url)

# get top tracks
st.write(f"### Most Popular Song NOW in {config.COUNTRY}")
top_song = song_scraper.get_top_track_by_geo("Singapore")
if 'Error' in top_song:
    st.write("Can't fetch any tracks")
else:
    for tr in top_song:
        url = tr['url']
        st.markdown(f"[{tr['name']}](%s)" % url)
