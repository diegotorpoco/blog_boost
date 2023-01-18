import streamlit as st 
import openai 
import gspread 
from google.oauth2 import service_account
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

def save_prompt(company_input,topic_input,name_input,prompt,tone='None',content=None):
    data = [company_input,topic_input,name_input,tone,prompt,content]
    sheet.append_row(data)

def test_v2(company_input,name_input,feature_desc=None,tone=None,content='Captions'):
    if content == 'Captions':
        prompt = company_input+'\n\n'+f"I want you to write a list of 5 engaging and hashtaggable Instagram captions for {name_input} based on the following description: {feature_desc} include possible emojis were fitted "
    else: #ideas                                                                                    
        prompt = company_input+'\n\n'+f"I want a list of instagram content ideas for {name_input} that have a {tone} tone"


    response_final = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1
        )
    return response_final


st.header("Generate Content For Instagram")

content = st.selectbox("What type of content would you like to create today?",['Captions','Ideas'])

if content == 'Captions':
    bis_name = st.text_input("What's your business name?","")
    bis_desc = st.text_area("Tell us a bit about your business","")
    feature_desc = st.text_area("Tell us about the post in need of a caption")
    button = st.button("Generate")
    
    if button:
        # st.write("Generating ideas")
        placeholder = st.empty()
        placeholder.write("Generating Captions")
        resp = test_v2(bis_desc,bis_name,feature_desc=feature_desc,content=content)
        placeholder.empty()
        st.write("Here are some are captions for your possible posts 📋")
        st.write(resp['choices'][0]['text'])
        save_prompt(bis_desc,feature_desc,bis_name,resp['choices'][0]['text'],tone='None',content=content)


if content == 'Ideas':
    bis_name = st.text_input("What's your business name?","")
    bis_desc = st.text_area("Tell us a bit about your business","")
    tone = st.selectbox("What tone would you like the idea to be: ",['Serious','Engaging','Friendly'])
    button = st.button("Generate")
    
    if button:
        placeholder = st.empty()
        placeholder.write("Generating Ideas")
        resp = test_v2(bis_desc,bis_name,tone=tone,content=content)
        placeholder.empty()
        st.write("Here are some are possible ideas for content in Instagram 👀")
        st.write(resp['choices'][0]['text'])
        save_prompt(bis_desc,feature_desc,bis_name,resp['choices'][0]['text'],tone=tone,content=content)


    

# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'])


# button = st.button("Done")
# if button:
#     st.write(options[0])

