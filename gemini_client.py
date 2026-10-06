import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

def get_client():
    if not API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Create a Gemini API key and put it in the local .env file."
        )
    return genai.Client(api_key=API_KEY)

def generate(prompt: str) -> str:
    client = get_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
