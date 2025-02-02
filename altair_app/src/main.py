from dotenv import load_dotenv
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
    """
    m_geminiParser = Geminiparser()
    m_PDFParser = PDFParser()

    #m_PDFParser.render_latex_to_PDF(Constants.Parsing.TEMP_TEX)
    #exit()

    #page_data = m_PDFParser.get_page_data("page1-5.pdf")
    page_data = m_PDFParser.get_page_data("1JC3-midterm-1.pdf") 

    extracted_questions = m_geminiParser.batch_extracted_questions(page_data, max_workers=2)

    remixed_questions = m_geminiParser.batch_remix_questions(flat_questions, max_workers=2)

    tex_str = m_PDFParser.build_tex_str(remixed_questions)
    tex_str = m_PDFParser.clean_latex(tex_str)
    #print("======")
    pyperclip.copy(tex_str)
    m_PDFParser.render_latex_to_PDF(tex_str)
    """

    app = QApplication(sys.argv)
    window = ThreeJsApp()
    window.show()
    sys.exit(app.exec())

    
