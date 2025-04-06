import streamlit as st
from PIL import Image
import json
import pandas as pd


st.set_page_config(page_title="Alola Region", page_icon="🌺")

st.title("🌺 Alola - The Hawaiian Region")

col1, col2 = st.columns(2)

with col1:
    st.image('data/Alola.png', caption="Alola Region, Pokémon Sun and Moon")

with col2:
    st.markdown("<div style='margin-top: 46px;'>", unsafe_allow_html=True)
    st.image('data/Oahu.jpg', caption="Oahu, Hawaii")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    The Alola Region...
    """
)

st.image('data/AlolaData.png')

#with open(pd dataframe)