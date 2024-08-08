import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

guest = True
  
while(guest):
    pergunta = input("O que deseja traduzir para emojis?\n")
    completion = openai.chat.completions.create(
        model='gpt-4',
        messages=[
        {"role": "system", "content":"Irei lhe encaminhar um texto e deverá traduzir este texto para emoji. Não utilize texto regular. Faça seu melhor utilizando emojis)};"},
        {"role": "user", "content": f"{pergunta}"}]
        , temperature=0.9,
        max_tokens=64,
        top_p=1
    )
    texto = completion.choices[0].message.content
    print(texto)
    guest = input ("deseja continuar perguntando? se sim digite 1 se não digite 0 \n")
