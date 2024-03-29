# Imports
import streamlit as st # Streamlit website
from random import choice # Pick a random song from a list
from PIL import Image # Load the favicon
from configs import * # Custom page styles
from lookup import url_to_title # Used for getting title of song from current URL
import time # Show instructions only temporarily

# Load favicon
favicon = Image.open('favicon.png')

# Name tab and show favicon
st.set_page_config(page_title="Musica en español", page_icon=favicon)

# Import and apply the custom styling configs
page_configs = [remove_st_ui, no_anchors, hide_settings, hide_made_with_s]
for custom_style in page_configs:
    st.markdown(custom_style, unsafe_allow_html=True)


# Pick a random song from 'songs.txt' (using list comprehension)
with open('songs.txt', 'r') as f:
    url = choice([link.strip() for link in f])

# Looks up the song name from the URL via a local dictionary and shows it above the video
st.title(url_to_title[url])

# Loads the video
st.video(url)

# Create three columns for content alignment
col1, col2, col3 = st.columns([1,2,1])

# Places control buttons
with col1:
    # Refresh button
    if st.button("🔄 Nueva canción"):
        st.rerun()

# Open in YouTube button
with col3:
    st.link_button("📺 Ver en YouTube", url)

# Gives instructions on how to play the video
with col2:
    instructions = st.empty()
    instructions.text("Haz clic en el vídeo para reproducirlo")
    time.sleep(5)
    instructions.empty()