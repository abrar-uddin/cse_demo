import streamlit as st

audio_file = open('recording.m4a', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/m4a')