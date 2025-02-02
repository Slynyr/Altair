from backend.gemini_parser import Geminiparser
from backend.pdf_parser import PDFParser
from backend.constants import Constants
import time


class GenManager: 
    def __init__(self):
        self.generated_papers = []
        self.m_PDFParser = PDFParser()

    def gen_paper(self, paper_path):
        m_geminiParser = Geminiparser()

        #Retrieving page Data
        page_data = self.m_PDFParser.get_page_data(file_path=paper_path)

        extracted_questions = m_geminiParser.batch_extracted_questions(page_data, max_workers=2)
        time.sleep(Constants.Parsing.SLEEP_TIME_BETWEEN_REMIX)
        remixed_questions = m_geminiParser.batch_remix_questions(extracted_questions, max_workers=2)

        tex_str = self.m_PDFParser.build_tex_str(remixed_questions)
        tex_str = self.m_PDFParser.clean_latex(tex_str)
        
        self.generated_papers.append(self.m_PDFParser.get_rendered_latex_to_PDF(tex_str))

    def preview_paper(self, index):
        print(index)
        self.m_PDFParser.render_pdf_to_browser(self.generated_papers[index])

    def get_latest_index(self):
        return len(self.generated_papers)-1