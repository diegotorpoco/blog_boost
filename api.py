import os
import openai
from constants import OPENAI_API_KEY
# openai.api_key = os.getenv(OPENAI_API_KEY)

BASE_PROMPT = "Write me a SEO optimized title and subcategories for a company that "

# COMPANY_INPUT = "helps oncological patients stick through their treatment thanks to a mobile app through specialized chatbot that sets reminders for patients for pills, fast communication with doctors, allows to store information about your physical/mental state and receive medical feedback from that. "

TOPIC_PROMPT = "Make it about: "

# TOPIC_INPUT = "'Mental Health'. "

FINAL_PROMPT = "Finally write a paragraph for every subcategory in the style of a short blogpost"



def test_v2(company_input,topic_input):
    openai.api_key = os.getenv(OPENAI_API_KEY)
    response_final = openai.Completion.create(
    model="text-davinci-003",
    prompt=BASE_PROMPT+company_input+TOPIC_PROMPT+topic_input+FINAL_PROMPT+'\n\n',
    temperature=0.9, #0.55 fue bueno
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1
    )
    return response_final