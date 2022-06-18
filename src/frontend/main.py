import streamlit as st
from src import config
from src.frontend.component.image_gallery import image_grid
from src.utils import song_scraper
from src.utils.util import name_generation
import pandas as pd

import datetime
hour = datetime.datetime.now().hour

greeting = "Good Morning" if 5<=hour<12 else "Good Afternoon" if 12<=hour<18 else "Good Evening"

# Set up webframe
st.set_page_config(page_title=config.PAGE_TITLE, layout="wide", initial_sidebar_state="auto")




# List of recommendation
user_list = name_generation(config.NUM_OF_USERS)
models =["CTR", "SoRec", "BPR"]
index = st.sidebar.selectbox("User List", range(len(user_list)), format_func=lambda x: user_list[x])
model_id = st.sidebar.selectbox("Model List", range(len(models)), format_func=lambda x: models[x])
num_artist = st.slider("Select Number of Artists for Recommendation", min_value=2, max_value=15)

user_name = user_list[index]
# st.write("index:", index)
st.title(config.TITLE)
st.write(f"""
    ### {greeting}, {user_name} ! 
    #### Personalized Music Recommendation
""")

image_grid(index, num_artist)

if model_id == 1:
    friends = ["Anh", "Linh", "Quan"]
    friend_id = st.sidebar.selectbox("Friend List", range(3), format_func=lambda x: friends[x])
    st.write(f"### Recommend for your friend, {friends[friend_id]}")
    image_grid(friend_id, num_artist)

# get top artist
st.write(f"Most Popular Artist in {config.COUNTRY}")
top_artist = song_scraper.get_top_artist_by_geo("Singapore")
if 'Error' in top_artist:
    st.write("Can't fetch any artists")
else:
    for tr in top_artist:
        url = tr['url']
        st.markdown(f"[- {tr['name']}](%s)" % url)


# get top tracks
st.write(f"Most Popular Song in {config.COUNTRY}")
top_song = song_scraper.get_top_track_by_geo("Singapore")
if 'Error' in top_song:
    st.write("Can't fetch any tracks")
else:
    for tr in top_song:
        url = tr['url']
        st.markdown(f"[- {tr['name']}](%s)" % url)
# st.balloons()
# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')
# genre_names = ['Dance Pop', 'Electronic', 'Electropop', 'Hip Hop', 'Jazz', 'K-pop', 'Latin', 'Pop', 'Pop Rap', 'R&B', 'Rock']
# audio_feats = ["acousticness", "danceability", "energy", "instrumentalness", "valence", "tempo"]


# def page():

#     with st.container():
#         col1, col2,col3,col4 = st.columns((2,0.5,0.5,0.5))
#         with col3:
#             st.markdown("***Choose your genre:***")
#             genre = st.radio(
#                 "",
#                 genre_names, index=genre_names.index("Pop"))
#         with col1:
#             st.markdown("***Choose features to customize:***")
#             start_year, end_year = st.slider(
#                 'Select the year range',
#                 1990, 2019, (2015, 2019)
#             )
#             acousticness = st.slider(
#                 'Acousticness',
#                 0.0, 1.0, 0.5)
#             danceability = st.slider(
#                 'Danceability',
#                 0.0, 1.0, 0.5)
#             energy = st.slider(
#                 'Energy',
#                 0.0, 1.0, 0.5)
#             instrumentalness = st.slider(
#                 'Instrumentalness',
#                 0.0, 1.0, 0.0)
#             valence = st.slider(
#                 'Valence',
#                 0.0, 1.0, 0.45)
#             tempo = st.slider(
#                 'Tempo',
#                 0.0, 244.0, 118.0)

#     tracks_per_page = 6
#     test_feat = [acousticness, danceability, energy, instrumentalness, valence, tempo]
#     uris, audios = n_neighbors_uri_audio(genre, start_year, end_year, test_feat)

#     tracks = []
#     for uri in uris:
#         track = """<iframe src="https://open.spotify.com/embed/track/{}" width="260" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>""".format(uri)
#         tracks.append(track)

#     if 'previous_inputs' not in st.session_state:
#         st.session_state['previous_inputs'] = [genre, start_year, end_year] + test_feat
    
#     current_inputs = [genre, start_year, end_year] + test_feat
#     if current_inputs != st.session_state['previous_inputs']:
#         if 'start_track_i' in st.session_state:
#             st.session_state['start_track_i'] = 0
#         st.session_state['previous_inputs'] = current_inputs

#     if 'start_track_i' not in st.session_state:
#         st.session_state['start_track_i'] = 0
    
#     with st.container():
#         col1, col2, col3 = st.columns([2,1,2])
#         if st.button("Recommend More Songs"):
#             if st.session_state['start_track_i'] < len(tracks):
#                 st.session_state['start_track_i'] += tracks_per_page

#         current_tracks = tracks[st.session_state['start_track_i']: st.session_state['start_track_i'] + tracks_per_page]
#         current_audios = audios[st.session_state['start_track_i']: st.session_state['start_track_i'] + tracks_per_page]
#         if st.session_state['start_track_i'] < len(tracks):
#             for i, (track, audio) in enumerate(zip(current_tracks, current_audios)):
#                 if i%2==0:
#                     with col1:
#                         components.html(
#                             track,
#                             height=400,
#                         )
#                         with st.expander("See more details"):
#                             df = pd.DataFrame(dict(
#                             r=audio[:5],
#                             theta=audio_feats[:5]))
#                             fig = px.line_polar(df, r='r', theta='theta', line_close=True)
#                             fig.update_layout(height=400, width=340)
#                             st.plotly_chart(fig)
            
#                 else:
#                     with col3:
#                         components.html(
#                             track,
#                             height=400,
#                         )
#                         with st.expander("See more details"):
#                             df = pd.DataFrame(dict(
#                                 r=audio[:5],
#                                 theta=audio_feats[:5]))
#                             fig = px.line_polar(df, r='r', theta='theta', line_close=True)
#                             fig.update_layout(height=400, width=340)
#                             st.plotly_chart(fig)

#         else:
#             st.write("No songs left to recommend")

# page()
