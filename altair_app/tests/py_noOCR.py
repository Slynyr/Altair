import pdfplumber
import os

PATH = os.path.abspath("/assets/sample.pdf")

with pdfplumber.open(PATH) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)