import os
import openai
from constants import OPENAI_API_KEY
# openai.api_key = os.getenv(OPENAI_API_KEY)

BASE_PROMPT_1 = "Write a 5 parragraphs essay about "
BASE_PROMPT_2 = "The essay should be linked to "
BASE_PROMPT_3 = "which is a "
BASE_PROMPT_4 = "Include a SEO optimized title. The style of the writing must be elegant but readable by a third grader. Separate the title from the blog."


def test_v2(company_input,topic_input,name_input):
    openai.api_key = os.getenv(OPENAI_API_KEY)
    response_final = openai.Completion.create(
    model="text-davinci-003",
    prompt=BASE_PROMPT_1+topic_input+BASE_PROMPT_2+name_input+BASE_PROMPT_3+company_input+BASE_PROMPT_4+'\n\n',
    temperature=0.9, #0.55 fue bueno
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1
    )
    return response_final