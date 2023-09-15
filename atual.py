import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Spotify Songs'
    )

df = pd.read_csv("genres_v2.csv")
df