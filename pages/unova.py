import streamlit as st
from PIL import Image
import json
import pandas as pd

st.set_page_config(page_title="Unova Region", page_icon="🗽")

st.title("🗽 Unova - The New York Region")

col1, col2 = st.columns(2)

with col1:
    st.image('data/Unova.png', caption="Unova Region, Pokémon Black and White")

with col2:
    st.markdown("<div style='margin-top: 70px;'>", unsafe_allow_html=True)
    st.image('data/NYC.jpg', caption="New York City, New York")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    The Unova Region...
    """
)

st.image('data/UnovaData.png')

