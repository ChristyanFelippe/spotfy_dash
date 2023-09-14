import streamlit as sl
import pandas as pd

df = pd.read_csv("01_Spotify.csv")
df[df["Stream"] > 1000000000]