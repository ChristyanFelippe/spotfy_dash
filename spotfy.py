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
    # coluna1, coluna2 = st.columns(2)
    # with coluna1:
    df.set_index("Track", inplace=True)

    artists = df["Artist"].value_counts().index

    artist = st.selectbox("Artista", artists)

    df_filtered = df[df["Artist"] == artist]

    st.bar_chart(df_filtered["Stream"])
    # df
    # with coluna2:
with aba3:
    