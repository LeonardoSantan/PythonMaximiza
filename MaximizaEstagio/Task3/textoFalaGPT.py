from pathlib import Path
import openai
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key
client = openai.OpenAI()
speech_file_path = Path(__file__).parent / f"{datetime.now()}.mp3"

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Léo, Dúvida, O que ser Caju? Eles vão me dar 577 em caju?"
)

# Salva o conteúdo da resposta diretamente no arquivo
with open(f"{datetime.now()}.mp3", "wb") as file:
    file.write(response.content)
