import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode()
        return f"data:image/png;base64,{b64_data}"

st.set_page_config(
    page_title="DataHacks25 ERC Enthusiasts",
    page_icon="🙂",
)

st.sidebar.success("Welcome to our Pokémon Audio Analysis Project!")
st.sidebar.markdown('# Main Page 🙂')
st.write("# Welcome to the ERC Enthusiasts Project for Datahacks 2025! 👋")



st.markdown(
    """
    In regards to the theme "Popular Culture" we decided on a project that focuses
    on the composition of Pokémon Soundtracks. Specifically, we trained a model to
    guess what genre and culture each games songs were based on. The model we used
    is called the Audio Spectagram Transformer Extractor (AST Extractor).
    """
)

st.markdown("<br><br>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.image('data/Diagram.jpg', caption='Data Analysis Pipeline')
with c2:
    st.image('data/Scatterplot.png', caption='Clusters Indicate Relation')



alola_img = get_base64_image("data/Alola.png")
galar_img = get_base64_image('data/Galar.jpg')
kalos_img = get_base64_image('data/Kalos.png')
paldea_img = get_base64_image('data/Paldea.png')
johto_img = get_base64_image('data/Johto.png')
unova_img = get_base64_image('data/Unova.png')

col1, col2 = st.columns([1,2])

with col1:
    st.markdown(
        f"""
        <a href="/alola" target="_self">
            <img src="{alola_img}" width="250" style="border-radius: 10px;">
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        Welcome to the Alola region! Inspired by **Hawaii**, we trained our model on
        Hawaiian music and ran it against music from the game where the Alola 
        region is featured, Pokémon Sun and Moon!
        """
    )

st.markdown("<br><br>", unsafe_allow_html=True)

col3, col4 = st.columns([1,2])

with col3:
    st.markdown(
        f"""
        <a href="/galar" target="_self">
            <img src="{galar_img}" width="250" style="border-radius: 10px;">
        </a>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        Our next stop is the cold and vibrant Galar region! Based on the **United
        Kingdom**, we chose classic **UK** rock to put against the algorithm. We then of
        course ran this model against the music from Pokémon Sword and Shield.
        """
    )

st.markdown("<br><br>", unsafe_allow_html=True)

col5, col6 = st.columns([1,2])

with col5:
    st.markdown(
        f"""
        <a href="/kalos" target="_self">
            <img src="{kalos_img}" width="250" style="border-radius: 10px;">
        </a>
        """,
        unsafe_allow_html=True
    )

with col6:
    st.markdown(
        """
        Moving on, we are now in the sunny and lively region of Kalos. This region
        is based on **France**. We noticed that the most popular music of France
        tended to be Jazz. After, we ran that model on the music from Pokémon X and 
        Y.
        """
    )

st.markdown("<br><br>", unsafe_allow_html=True)

col7, col8 = st.columns ([1,2])

with col7:
    st.markdown(
        f"""
        <a href="/paldea" target="_self">
            <img src="{paldea_img}" width="250" style="border-radius: 10px;">
        </a>
        """,
        unsafe_allow_html=True
    )

with col8:
    st.markdown(
        """
        The region of Paldea is based on the warm and bustling country of **Spain**.
        We chose Latin music, since it's the most popular in Spain, and ran that
        against our model. The game that Paldea is from is Pokémon Scarlet and Violet.
        """
    )

st.markdown("<br><br>", unsafe_allow_html=True)

col9, col10 = st.columns ([1,2])

with col9:
    st.markdown(
        f"""
        <a href="/johto" target="_self">
            <img src="{johto_img}" width="250" style="border-radius: 10px;">
        </a>
        """,
        unsafe_allow_html=True
    )

with col10:
    st.markdown(
        """
        Now in Johto, the region inspired by the Kansai Region of Japan. This region
        is known for their large Pagodas and rich culture. The music of Pokémon Gold
        and Silver reflects that, with a very rich Japanese sound.
        """
    )

st.markdown("<br><br>", unsafe_allow_html=True)

col11, col12 = st.columns ([1,2])

with col11:
    st.markdown(
        f"""
        <a href="/unova" target="_self">
            <img src="{unova_img}" width="250" style="border-radius: 10px;">
        </a>
        """,
        unsafe_allow_html=True
    )

with col12:
    st.markdown(
        """
        Finally our last destination is Unova, based on the state of New York this
        region is vibrant and full of life. The music of New York is especially rich
        and reflects its culture remarkably. As such, the music of Pokémon Black and
        White tries its best to emulate the feel of New York and American music in
        general.
        """
    )