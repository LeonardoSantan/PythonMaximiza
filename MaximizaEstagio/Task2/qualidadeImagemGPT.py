import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

response = openai.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
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
                        "url": "https://store-images.s-microsoft.com/image/apps.42049.13715845469587517.60dedf91-7527-4ab4-8e98-0071e0f068f6.8c7b5656-7baf-438e-b6b0-322051df5d5b?q=90&w=177&h=265",
                        "detail": "low"
                    }
                }
            ]
        }
    ],
    max_tokens=300
)

print(response.choices[0].message.content)
