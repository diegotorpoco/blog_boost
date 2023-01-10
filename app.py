import streamlit as st 
import openai
from PIL import Image
from mock_medium import image_gen
import numpy as np
from streamlit_card import card

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
    )

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


with st.container():
    st.subheader("Hola emprendedores :wave: somos Bruno:owl: y Diego:robot_face:")
    st.title("Nula KIT")
    st.write("Entiendemos que a veces puede ser difícil encontrar ideas para crear contenido en línea, especialmente cuando la inspiración es nula.")
    st.write("Hemos creado Nula Kit las cuales van a ser una serie de herramientas para ayudarte a escribir tu contenido :sparkling_heart:.")
    st.write("##")
    


col1, col2, col3 = st.columns(3, gap="small")

with col1:

    card(
    title="Instagram",
    text="Ads, posts, bios y DMs!",
    image="https://eltallerdehector.com/wp-content/uploads/2022/06/cd939-logo-instagram-png.png",
    url="http://localhost:8501/Instagram",
    )
   

with col2:
   
   card(
    title="Blogs",
    text="Ideas, titulos y blogs!",
    image="https://cdn.mos.cms.futurecdn.net/uazw6gFQuEC29mxMM55Tpb.jpg",
    url="http://localhost:8501/Blogs",
    )

with col3:
   
   card(
    title="Coming soon!",
    text="Cuentanos qué quisieras :)",
    image="https://st.depositphotos.com/1654249/4904/i/600/depositphotos_49041297-stock-photo-3d-man-squatting-and-confusing.jpg",
    url="https://www.google.com",
    )


with st.container():
    st.write("---")
    st.header("Escríbenos qué piensas!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/164691b315ff3023a9238892c3d2528f" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="Correo" required>
        <textarea name="message" placeholder="Mensaje" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()