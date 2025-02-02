from backend.gemini_parser import Geminiparser
from dotenv import load_dotenv
from backend.constants import Constants
import base64


def temp_read(file_path):
    with open(file_path, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

    return doc_data


load_dotenv()

def __main__():
    m_geminiParser = Geminiparser()

    temp_data = temp_read("page-5.pdf")

    print(m_geminiParser.remix_questions(Constants.Gemini.TEMP_QUESTION))

__main__()
    
