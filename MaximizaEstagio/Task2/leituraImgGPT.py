import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content": [
                {
                    "type": "text", "text": "O que há nesta imagem?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.kitguru.net/wp-content/uploads/2020/03/D1B9C77C-8B13-4FD0-86EB-72B1A44AA5C1.png"
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)


print(completion.choices[0].message.content)
