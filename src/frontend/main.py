import streamlit as st
from src import config
from src.frontend.component.image_gallery import image_grid
import pandas as pd

import datetime
hour = datetime.datetime.now().hour

greeting = "Good Morning" if 5<=hour<12 else "Good Afternoon" if 12<=hour<18 else "Good Evening"

# Set up webframe
st.set_page_config(page_title=config.PAGE_TITLE, layout="wide", initial_sidebar_state="auto")




# List of recommendation
user_list = ["Quan Nguyen", "Linh Vu", "Anh Nguyen"]

user_name = st.sidebar.selectbox("Select User", user_list)
st.title(config.TITLE)
st.write(f"""
    ### {greeting}, {user_name} ! 
    #### Personalized Music Recommendation
""")

image_grid()


st.balloons()
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
