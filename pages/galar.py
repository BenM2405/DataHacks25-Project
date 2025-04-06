import streamlit as st
from PIL import Image
import json
import pandas as pd


st.set_page_config(page_title="Galar Region", page_icon="💂")

st.title("💂 Galar - The United Kingdom Region")

col1, col2 = st.columns(2)

with col1:
    st.image('data/Galar.jpg', caption="Galar Region, Pokémon Swod and Shield")

with col2:
    st.markdown("<div style='margin-top: 21px;'>", unsafe_allow_html=True)
    st.image('data/UK.png', caption="Britain, United Kingdom")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    The Galar region...
    """
)

st.image('data/GalarData.png')