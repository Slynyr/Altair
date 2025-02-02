from backend.gemini_parser import Geminiparser
from dotenv import load_dotenv
from backend.constants import Constants
from backend.pdf_parser import PDFParser
import base64
import sys
from PyQt6.QtWidgets import QApplication
from backend.threejs_app import ThreeJsApp


def temp_read(file_path):
    with open(file_path, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

    return doc_data


load_dotenv()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThreeJsApp()
    window.show()
    sys.exit(app.exec())

    m_geminiParser = Geminiparser()
    m_PDFParser = PDFParser()

    temp_data = m_PDFParser.get_page_data("full-test.pdf")

    extracted_question = m_geminiParser.extract_questions(temp_data[4])[0]
    print(m_geminiParser.remix_questions(extracted_question))
    
