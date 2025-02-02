from backend.gemini_parser import Geminiparser
import base64

def temp_read(file_path):
    with open(file_path, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

    return doc_data



def __main__():
    m_geminiParser = Geminiparser()

    temp_data = temp_read("page-1.pdf")

    q_list = m_geminiParser.extract_questions(temp_data)