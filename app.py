import streamlit as st 
import openai
#Set title and subtitle
BASE_PROMPT = "Write me a SEO optimized title and subcategories for "
TOPIC_PROMPT = "Consider the following keyword for the title and subcategories: "
FINAL_PROMPT = "Finally write a paragraph for every subcategory in the style of a short blogpost"
openai.api_key = st.secrets['api']


def test_v2(company_input,topic_input):
    response_final = openai.Completion.create(
    model="text-davinci-003",
    prompt=BASE_PROMPT+company_input+TOPIC_PROMPT+topic_input+FINAL_PROMPT+'\n\n',
    temperature=0.85, #0.55 fue bueno
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1
    )
    return response_final


st.title("Blog Boost")
st.subheader("Blog Boost allows SMBs to create content in order to increase website traffic.")


# Add a textbox and store the input in a variable
company_input = st.text_area("What is your business about?","",height=5,disabled=False,
placeholder="Buildspace is a e-learning community-driven webiste, that aids builders to unite and explore promising domains and ship meaningful products ")

topic_input = st.text_area("include the topic of the blog you want: ","",height=5,disabled=False,
placeholder="Edtech, Community, Web3, AI")

if st.button("Generate Blog"):  
# if (company_input) and (topic_input):
    resp = test_v2(company_input=company_input,topic_input=topic_input)
    st.write(resp['choices'][0]['text'])
