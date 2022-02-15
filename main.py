import streamlit as st
from streamlit_player import st_player


st_player("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

audio_file = open('recording.m4a', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/m4a')