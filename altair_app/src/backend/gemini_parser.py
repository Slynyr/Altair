import google.generativeai as genai
import os
from backend.constants import Constants

class Geminiparser:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash-exp")

    def extract_questions(self, page_data):
        response = self.model.generate_content([{'mime_type': 'application/pdf', 'data': page_data}, Constants.Gemini.EXTRACT_PROMPT])

    def remix_questions(self, question):
        response = self.model.generate_content([
            {"role": "user", "parts": [{"text": f"{Constants.Gemini.REMIX_PROMPT}\n\n{question}"}]}
        ])


        return response.text