import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Spotify Songs'
    )
st.title("Dashboard Spotify :musical_note:")

aba1, aba2, aba3 = st.tabs(['List', 'Filter', 'Dashboard'])
df = pd.read_csv("01_Spotify.csv")


with aba1:
    st.dataframe(df)
with aba2:
    df.set_index("Track", inplace=True)
    
    artists = df["Artist"].value_counts().index
    artist = st.sidebar.selectbox("Artista", artists)
    df_filtered = df[df["Artist"] == artist]
    display_songs = st.sidebar.checkbox('Display Songs')
    albuns = df_filtered["Album"].value_counts().index
    album = st.sidebar.selectbox("Album", albuns)
    df_filtered_albuns = df[df["Album"] == album]
    display_albuns = st.sidebar.checkbox('Display Dashboard')

    if display_songs:
        st.write(artist)
        st.bar_chart(df_filtered["Stream"])
    if display_albuns:
        st.bar_chart(df_filtered_albuns["Album"])

with aba3:
    df.set_index("Artist", inplace=True)
    st.bar_chart(df[df["Stream"] > 1_500_000_000]["Stream"])