import google.generativeai as genai
import os
from backend.constants import Constants
from concurrent.futures import ThreadPoolExecutor, as_completed

class Geminiparser:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash-exp")

    def extract_questions(self, page_data):
        response = self.model.generate_content([{'mime_type': 'application/pdf', 'data': page_data}, Constants.Gemini.EXTRACT_PROMPT])
        q_list = response.text.split("crodie")
        
        print("Extracted Page")
        return q_list

    def remix_questions(self, question):
        response = self.model.generate_content([
            {"role": "user", "parts": [{"text": f"{Constants.Gemini.REMIX_PROMPT}\n\n{question}"}]}
        ])

        print("Remixed Question")
        return response.text
    
    def batch_extracted_questions(self, pages_data, max_workers=15):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_page = {executor.submit(self.extract_questions, page): page for page in pages_data}

            results = []

            for future in as_completed(future_to_page):
                try:
                    results.append(future.result())
                except Exception as e:
                    print(f"Error processing page {e}")

            return results
        
    def batch_remix_questions(self, questions, max_workers=15):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_question = {executor.submit(self.remix_questions, q): q for q in questions}
            results = []

            for future in as_completed(future_to_question):
                try:
                    results.append(future.result())
                except Exception as e:
                    print(f"Error remixing question: {e}")
            
            return results
                
