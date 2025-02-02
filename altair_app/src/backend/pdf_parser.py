"""create a class that takes a pdf file and saves first page as a new pdf output"""
import webbrowser
import PyPDF2
import io
import base64
import re
import tempfile
import subprocess
import os 
from backend.constants import Constants
from pylatex import Document

class PDFParser:
    def __init__(self):
        pass
    
    
    def get_page_data(self, file_path):
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()

            if len(reader.pages) == 0:
                print("PDF is empty")
                return []
            
            output_data = []
            
            for i in range(0, len(reader.pages)):
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[i])

                output_stream = io.BytesIO()
                writer.write(output_stream)
                output_stream.seek(0)

                base64_encoded = base64.b64encode(output_stream.getvalue()).decode('utf-8')
                output_data.append(base64_encoded)
        return output_data

    def build_tex_str(self, remixed_questions):
        output = ""
        for question in remixed_questions:
            output += f"{question}\n"

        return output

    def clean_latex(self, latex_text):
        #TODO: TUNE CLEANING
        pattern = "|".join(map(re.escape, Constants.Parsing.LATEX_BLACKLIST))
        latex_text = re.sub(pattern, "", latex_text)

        return latex_text
    
    def get_rendered_latex_to_PDF(self, latex_text, output_filename="output.pdf"):
        with open(Constants.Parsing.TEX_TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template_content = f.read()

        processed_latex = template_content.replace("<<<CONTENT>>>", latex_text)

        with tempfile.TemporaryDirectory() as temp_dir:
            tex_path = os.path.join(temp_dir, "document.tex")

            with open(tex_path, "w", encoding="utf-8") as f:
                f.write(processed_latex)

            subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", temp_dir, tex_path], check=True)

            with open(os.path.join(temp_dir, "document.pdf"), "rb") as f:
                pdf_data = f.read()

        return pdf_data
    
    def render_pdf_to_browser(self, pdf_data):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(pdf_data)
            tmp_file_path = tmp_file.name
        webbrowser.open('file://' + tmp_file_path)