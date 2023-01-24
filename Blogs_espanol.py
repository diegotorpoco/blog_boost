import streamlit as st 
import openai
from PIL import Image
# from mock_medium import image_gen
import numpy as np
import gspread 
from google.oauth2 import service_account

# Set title and subtitle
openai.api_key = st.secrets['api']

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)

sheet_url = st.secrets["private_gsheets_url"]
gc = gspread.authorize(credentials=credentials)
spreadsheet = gc.open_by_url(sheet_url)
sheet = spreadsheet.get_worksheet(0)

def save_prompt(company_input,topic_input,name_input,tone,prompt):
    data = [company_input,topic_input,name_input,tone,prompt]
    sheet.append_row(data)

st.set_page_config(
    initial_sidebar_state="collapsed"
    )

def test_v2(company_input,topic_input,name_input,tone):
    BASE_PROMPT_1 = "Escribe un ensayo de 5 parrafos sobre "
    BASE_PROMPT_2 = "El tema del ensayo debe estar relacionado a  "
    BASE_PROMPT_3 = "que es una "
    BASE_PROMPT_4 = f"Incluye un título optimizado por SEO. El estilo de escritura debe ser elegante pero entendible por una persona de 10 años de edad. Separa el título del ensayo y que el título sea corto. Quiero que el tono de comunicación sea {tone}"
    response_final = openai.Completion.create(
    model="text-davinci-003",
    prompt=BASE_PROMPT_1+topic_input+BASE_PROMPT_2+name_input+BASE_PROMPT_3+company_input+BASE_PROMPT_4+'\n\n',
    temperature=0.85, #0.55 fue bueno
    max_tokens=1012,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1
    )
    return response_final


st.title("Genera artículos de blog para tu empresa de manera rápida y sencilla")

st.markdown("""
1. Describe detalladamente a qué se dedica tu empresa 💼
2. Escoge un tema para el articulo 📝 
3. Listo 🤗
""")


# Add a textbox and store the input in a variable
name_input = st.text_area("Nombre de tu compañia: ","",height=5,disabled=False,
placeholder="Microsoft, Facebook, Tesla")

company_input = st.text_area("Que hace tu empresa?","",height=5,disabled=False,
placeholder="Microsoft es una empresa de tecnología que desarrolla y comercializa software, sistemas operativos, dispositivos y servicios en línea")

topic_input = st.text_area("Escribe el tema del articulo que deseas realizar: ","",height=5,disabled=False,
placeholder="IA, Educacion, Inteligencia Artificial Aplicado al sector Educacion")

tone = st.selectbox("Como te gustaria que fuera el tono del articulo: ",['atractivo','serio','comico'])



if st.button("Generando Articulo"):  
    with st.spinner('Espera Porfavor...'):
        resp = test_v2(company_input=company_input,topic_input=topic_input,name_input=name_input,tone=tone)
        st.write(resp['choices'][0]['text'])
        save_prompt(company_input=company_input,topic_input=topic_input,name_input=name_input,tone=tone,prompt=resp['choices'][0]['text'])
