import streamlit as st
from src import config
import pandas as pd

# Set up webframe
st.set_page_config(page_title=config.PAGE_TITLE, layout="wide")

st.title(config.TITLE)
st.write("""
    ### Welcome to Last FM
""")

# List of recommendation
artist_list = ["Moi dix Mois", "Bella Morte"]

artist_name = st.sidebar.selectbox("Select Artist", artist_list)
st.write(f"{artist_name} selected")


# Visualize aritst
print(config.ARTIST_IMAGE_PATH)
image_path_df = pd.read_csv(config.ARTIST_IMAGE_PATH)
image_path = image_path_df[image_path_df["artist_name"]==artist_name]["image_path"].values[0]

st.image(image_path, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")



