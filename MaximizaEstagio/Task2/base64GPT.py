import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


image_path = "/home/oem/Imagens/D1B9C77C-8B13-4FD0-86EB-72B1A44AA5C1.png"

base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "O que há nesta imagem, qual personagem da mesma?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64, {base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}
response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['choices'][0]['message']['content'])
else:
    print(f"Erro: {response.status_code}")
    print(response.json())
