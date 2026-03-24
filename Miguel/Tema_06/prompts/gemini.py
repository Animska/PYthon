import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not GEMINI_API_KEY:
    raise ValueError("La variable de entorno GEMINI_API_KEY no esta definida")

cliente= genai.Client(api_key=GEMINI_API_KEY)

def enviar_mensaje(contenido:str)->str:
    response = cliente.models.generate_content(
        model = GEMINI_MODEL,
        contents = contenido
    )
    return response.text or ""

print(enviar_mensaje("Cual es la capital de España"))