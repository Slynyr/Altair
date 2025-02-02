import os
import google.generativeai as genai

import base64

genai.configure(api_key="AIzaSyAbjIin19CHf7TZlnafplsoRHdfAZVn6Dk")
model = genai.GenerativeModel("gemini-2.0-flash-exp")
doc_path = "page-2.pdf" # Replace with the actual path to your local PDF

# Read and encode the local file
with open(doc_path, "rb") as doc_file:
    doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

prompt = "Give me all the question in this paper in latex form. Please spend extra time ensuring that any existing equations are correctly identified. Please include the question itself and any formulas if any. Do not provide any additional text in your response that is not in the paper"

response = model.generate_content([{'mime_type': 'application/pdf', 'data': doc_data}, prompt])

print(response.text)
print(response.usage_metadata)