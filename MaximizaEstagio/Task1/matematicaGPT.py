import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

completion = openai.chat.completions.create(

model='gpt-4',

messages=[

{"role": "system", "content": "Você é um professor de história muito ruim em matemática"},
{"role": "user", "content": "qual a tabuada do 5?"}])

# print(completion.choices[0].message)
print(completion.choices[0].message.content)
