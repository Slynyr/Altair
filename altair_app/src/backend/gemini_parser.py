import google.generativeai as genai
import os

class Geminiparser:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash-exp")

    def extract_questions(self, page_data):
        pass

    def remix_questions(self, question):
        response = self.model.generate_content([{'mime_type': 'text/plain', 'data': question}, Constants.Gemini.REMIX_PROMPT])