import streamlit as st
from PIL import Image
import json
import pandas as pd



st.set_page_config(page_title="Paldea Region", page_icon="🐂")

st.title("🐂 Paldea - The Spanish Region")

col1, col2 = st.columns(2)

with col1:
    st.image('data/Paldea.png', caption="Paldea Region, Pokémon Scalet and Violet")

with col2:
    st.markdown("<div style='margin-top: 50px;'>", unsafe_allow_html=True)
    st.image('data/Spain.jpg', caption="Barcelona, Spain")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    The Paldea Region...
    """
)

st.image('data/PaldeaData.png')

#with open(pd dataframe)