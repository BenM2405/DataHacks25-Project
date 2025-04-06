import streamlit as st
from PIL import Image
import json
import pandas as pd


st.set_page_config(page_title="Kalos Region", page_icon="🥐")

st.title("🥐 Kalos - The French Region")

col1, col2 = st.columns(2)

with col1:
    st.image('data/Kalos.png', caption="Kalos Region, Pokémon X and Y")

with col2:
    st.image('data/France.jpg', caption="Paris, France")


st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    The Kalos Region...
    """
)

st.image('data/KalosData.png')

#with open(pd dataframe)