import streamlit as st
from PIL import Image
import json
import pandas as pd

st.set_page_config(page_title="Johto Region", page_icon="⛩️")

st.title("⛩️ Johto - The Kansai Region")


col1, col2 = st.columns(2)

with col1:
    st.image('data/Ecruteak.png', caption="Johto Region, Pokémon Gold, Silver, and Crystal")

with col2:
    st.markdown("<div style='margin-top: 82px;'>", unsafe_allow_html=True)
    st.image('data/Kansai.jpg', caption="Kansai Region, Japan")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    The region of Johto...
    """
)

st.image('data/JohtoData.png')

#with open(pd dataframe)