import streamlit as st

st.title("Last FM")
st.write("""
    ### Welcome to Last FM
""")

artist_name = st.sidebar.selectbox("Select Artist", ("My Tam", "Taylor Script"))
st.write(f"{artist_name} selected")