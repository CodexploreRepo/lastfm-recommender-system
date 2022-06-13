import streamlit as st
from src import config
import pandas as pd
from src.utils import song_scraper


# Set up webframe
st.set_page_config(page_title=config.PAGE_TITLE, layout="wide")

st.title(config.TITLE)
st.write("""
    ### Welcome to Last FM
""")

# List of recommendation
artist_list = ["Moi dix Mois", "Bella Morte"]

artist_name = st.sidebar.selectbox("Select Artist", artist_list)
# st.write(f"{artist_name} selected")


# Visualize aritst
print(config.ARTIST_IMAGE_PATH)
image_path_df = pd.read_csv(config.ARTIST_IMAGE_PATH)
image_path = image_path_df[image_path_df["artist_name"]==artist_name]["image_path"].values[0]

st.image(image_path, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

## Get top song by selected artist
st.write(f"Top {config.LIMIT_TOP_SONG} song by {artist_name}")
tracks = song_scraper.get_top_track_by_artist(artist_name)
# if calling api failed
if 'Error' in tracks:
    st.write("Can't fetch any song")
else:
    for tr in tracks:
        url = tr['url']
        st.markdown(f"[{tr['name']}](%s)" % url)
