import streamlit as st 
import openai 
import gspread 
from google.oauth2 import service_account
import gspread 
from google.oauth2 import service_account

openai.api_key = st.secrets['api']


PROMPT_TIKTOK = """
Te voy a dar una [descripción de una empresa] y luego requiero que me crees un guión de 30 segundos a 1 minuto para un video de tiktok que tendra un [fin especifico]. 
Finalmente requiero que me entregues el guion en una tabla de 2 columnas, la primera columna sera la escena (que SIEMPRE tenga ideas para cada escena del guion especificas) y la columna 2 denominada descripción del guión que contenga la información para realizar la escena.

descripción de una empresa: {desc_emp}.
fin especifico: {fin}.

Usa este formato:
Escena | Descripcion del guión

"""
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


def test_v2(desc_emp,fin,content='TikTok'):
    response_final = openai.Completion.create(
        model="text-davinci-003",
        prompt=PROMPT_TIKTOK.format(desc_emp=desc_emp,fin=fin),
        temperature=0.8,
        max_tokens=1400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1
        )
    return response_final


def save_prompt_tiktok(desc_emp,
                       fin,
                       emp_name,
                       prompt,
                       tone='None',
                       content='TikTok'):
    data = [desc_emp,fin,emp_name,tone,prompt,content]
    sheet.append_row(data)


st.header("Crea un guion de tiktok en un par de segundos!")
st.markdown("""
1. Describe a que se dedica tu empresa/emprendimiento/canal
2. Cuentanos sobre el tema del tiktok que requieres hacer
3. Listo 🤗
""")

emp_name = st.text_input("¿Cómo se llama tu canal/empresa/emprendimiento?")
desc_emp = st.text_area("Cuéntanos que hace tu empresa/emprendimiento/canal","")
fin = st.text_area("¿De qué se trata el video?","")

button = st.button("Presiona aca para generar tu guión")

if button:
    placeholder = st.empty()
    placeholder.write("Generando Descripciones")
    resp = test_v2(desc_emp=desc_emp,fin=fin)
    placeholder.empty()
    st.write("Aca hay una idea para el guión de tu tiktok")
    st.write("\n\n")
    st.write("Escena | Descripción de la escena")
    st.write(resp['choices'][0]['text'])
    save_prompt_tiktok(desc_emp,fin,emp_name,resp['choices'][0]['text'],tone='None')
