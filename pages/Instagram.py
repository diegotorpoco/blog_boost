import streamlit as st 
import openai
from PIL import Image
from mock_medium import image_gen
import numpy as np
from streamlit_card import card
import gspread 
from google.oauth2 import service_account

#Set title and subtitle
BASE_PROMPT_1 = "Write a 5 parragraphs essay about "
BASE_PROMPT_2 = "The essay should be linked to "
BASE_PROMPT_3 = "which is a "
BASE_PROMPT_4 = "Include a SEO optimized title. The style of the writing must be elegant but readable by a third grader. Separate the title from the blog, and keep the title short."
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

def save_prompt(company_input,topic_input,name_input,prompt):
    data = [company_input,topic_input,name_input,prompt]
    sheet.append_row(data)

st.set_page_config(
    initial_sidebar_state="collapsed"
    )

def test_v2(company_input,topic_input,name_input):
    response_final = openai.Completion.create(
    model="text-davinci-003",
    prompt=BASE_PROMPT_1+topic_input+BASE_PROMPT_2+name_input+BASE_PROMPT_3+company_input+BASE_PROMPT_4+'\n\n',
    temperature=0.85, #0.55 fue bueno
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1
    )
    return response_final


st.title("Instagram Boost")
st.subheader("Instagram Boost allows SMBs to create content in order to increase website traffic.")

### CAMBIOS LALALA

# Add a textbox and store the input in a variable
company_input = st.text_area("What is your business about?","",height=5,disabled=False,
placeholder="Buildspace is a e-learning community-driven webiste, that aids builders to unite and explore promising domains and ship meaningful products ")

topic_input = st.text_area("include the topic of the blog you want: ","",height=5,disabled=False,
placeholder="Edtech, Community, Web3, AI")

name_input = st.text_area("include the name of your company: ","",height=5,disabled=False,
placeholder="Buildspace, Facebook, Tesla")


if st.button("Generate Blog"):  
    # if (company_input) and (topic_input):
    with st.spinner('Wait for it...'):
        resp = test_v2(company_input=company_input,topic_input=topic_input,name_input=name_input)
        st.write(resp['choices'][0]['text'])
        save_prompt(company_input=company_input,topic_input=topic_input,name_input=name_input,prompt=resp['choices'][0]['text'])
        texto_comp = resp['choices'][0]['text'][2:-1]
        if "\n" in texto_comp:
            index = texto_comp.find("\n")
        titulo = texto_comp[6:index]
        texto = texto_comp[index+2:-1]
        
        link = image_gen(titulo, "Prueba12345", texto, name_input, company_input, url_base='C:/Users/bruno/Desktop/Drive/Bruno/SEO/blog_boost/')
        #link = image_gen("prueba", "Prueba12345", "texto", name_input, company_input, url_base='C:/Users/bruno/Desktop/Drive/Bruno/SEO/blog_boost/')
        # imagennn = Image.open(link)
        st.image(np.asarray(link))
        st.success('Done!')