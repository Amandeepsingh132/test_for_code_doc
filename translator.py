import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class Translator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY in environment.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def translate(self, text: str, target_language: str) -> str:
        prompt = f"Translate the following text to {target_language}:\n\n{text}"
        response = self.model.generate_content(prompt)
        return response.text.strip()
