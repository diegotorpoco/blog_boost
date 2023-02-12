import streamlit as st 
import openai 
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


def generate_reel_tiktok(desc_emp,fin):
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

def test_v2(company_input,name_input,feature_desc=None,tone=None,content='Descripcion Para Publicacion'):
    if content == 'Descripcion Para Publicacion':
        prompt = company_input+'\n\n'+f"Haz una lista con 5 descripciones atractivas y con hashtags para una publicación de Instagram de la empresa descrita anteriormente. La publicación va a ser sobre {feature_desc}. SIEMPRE incluye dos emojis distintos en el texto, y al final del texto hashtag que esten en español."
    else:                                                                                    
        prompt = company_input+'\n\n'+f"Haz una lista con 8 ideas para contenido de Instagram para la empresa descrita anteriormente. Que sean para generar mas {tone}"


    response_final = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1
        )
    return response_final

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

def save_prompt(company_input,topic_input,name_input,prompt,tone='None',content=None):
    data = [company_input,topic_input,name_input,tone,prompt,content]
    sheet.append_row(data)

def save_prompt_tiktok(desc_emp,
                       fin,
                       emp_name,
                       prompt,
                       tone='None',
                       content='TikTok'):
    data = [desc_emp,fin,emp_name,tone,prompt,content]
    sheet.append_row(data)



st.header("Crea Contenido de Instagram para tu Negocio Sin Esfuerzo")
st.markdown("""
1. Elige qué servicio deseas: 💡 ideas de contenido  📝 descripciones para tus publicaciones 🎥 Guion para Reel
2. Describe detalladamente a qué se dedica tu empresa 💼
3. Si elegiste ideas, elige el fin que deseas lograr 🎯. Si elegiste descripciones, describe la publicación 📷. Si elegiste guión, describe el video 🎬 

Listo 🤗

""")

content = st.selectbox("Que servicio desea?",['Descripcion Para Publicacion','Ideas','Guion para reels'])


if content == 'Descripcion Para Publicacion':
    bis_name = st.text_input("Como se llama tu empresa?","")
    bis_desc = st.text_area("Cuentanos que hace tu empresa","")
    feature_desc = st.text_area("Cuentanos sobre la publicación")
    button = st.button("Generate")
    
    if button:
        placeholder = st.empty()
        placeholder.write("Generando Descripciones")
        resp = test_v2(bis_desc,bis_name,feature_desc=feature_desc,content=content)
        placeholder.empty()
        st.write("Aca hay algunas posibles descripciones para tu publicacion 📋")
        st.write(resp['choices'][0]['text'])
        save_prompt(bis_desc,feature_desc,bis_name,resp['choices'][0]['text'],tone='None',content=content)



if content == 'Ideas':
    bis_name = st.text_input("Como se llama tu empresa?","")
    bis_desc = st.text_area("Cuentanos que hace tu empresa","")
    tone = st.selectbox("Cual es el fin de la idea: ",['interacciones','exposicion','ventas'])
    button = st.button("Generate")
    
    if button:
        placeholder = st.empty()
        placeholder.write("Generando Ideas")
        resp = test_v2(bis_desc,bis_name,tone=tone,content=content)
        placeholder.empty()
        st.write("Aca hay algunas ideas para crear contenido en instagram 👀")
        st.write(resp['choices'][0]['text'])
        save_prompt(bis_desc,'None',bis_name,resp['choices'][0]['text'],tone=tone,content=content)


if content == 'Guion para reels':
    emp_name = st.text_input("¿Cómo se llama tu canal/empresa/emprendimiento?")
    desc_emp = st.text_area("Cuéntanos que hace tu empresa/emprendimiento/canal","")
    fin = st.text_area("¿De qué se trata el video?","")
    button = st.button("Presiona aca para generar tu guión")

 
    if button:
        placeholder = st.empty()
        placeholder.write("Generando Descripciones")
        resp = generate_reel_tiktok(desc_emp=desc_emp,fin=fin)
        placeholder.empty()
        st.write("Aca hay una idea para el guión de tu tiktok")
        st.write("\n\n")
        st.write("Escena | Descripción de la escena")
        st.write(resp['choices'][0]['text'])
        save_prompt_tiktok(desc_emp,fin,emp_name,resp['choices'][0]['text'],tone='None',content=content)
