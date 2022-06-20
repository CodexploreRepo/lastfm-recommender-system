from PIL import Image
import streamlit as st
from src import config

def display_logo(img_name='dito.png'):
    img = Image.open(config.IMAGES/img_name)
    img.thumbnail((130,100))
    col1, col2, col3 = st.sidebar.columns([1,20,1])

    with col1:
        st.write("")
    with col2:
        st.image(img)
    with col3:
        st.write("")