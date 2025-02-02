from backend.gemini_parser import Geminiparser
from dotenv import load_dotenv
from backend.constants import Constants
from backend.pdf_parser import PDFParser
import base64
import sys
from PyQt6.QtWidgets import QApplication
from backend.threejs_app import ThreeJsApp
import pyperclip

def temp_read(file_path):
    with open(file_path, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

    return doc_data


load_dotenv()

if __name__ == "__main__":
    print("Im happening")

    m_geminiParser = Geminiparser()
    m_PDFParser = PDFParser()

    page_data = m_PDFParser.get_page_data("half-test.pdf")

    extracted_questions = m_geminiParser.batch_extracted_questions(page_data, max_workers=3)
    print(len(extracted_questions))

    flat_questions = [q for q_list in extracted_questions for q in q_list]
    print(len(flat_questions))
    remixed_questions = m_geminiParser.batch_remix_questions(flat_questions, max_workers=3)

    app = QApplication(sys.argv)
    window = ThreeJsApp()
    window.show()
    sys.exit(app.exec())

    
