import streamlit as st
import pandas as pd

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets\male_players.csv", index_col=0)
    st.session_state["data"] = df_data