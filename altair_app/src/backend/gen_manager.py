from backend.gemini_parser import Geminiparser
from backend.pdf_parser import PDFParser


class GenManager: 
    def __init__(self):
        pass

    def gen_paper(self, paper_path):
        m_geminiParser = Geminiparser()
        m_PDFParser = PDFParser()

        #Retrieving page Data
        page_data = m_PDFParser.get_page_data(file_path=paper_path)

        extracted_questions = m_geminiParser.batch_extracted_questions(page_data, max_workers=2)
        remixed_questions = m_geminiParser.batch_remix_questions(extracted_questions, max_workers=2)

        tex_str = m_PDFParser.build_tex_str(remixed_questions)
        tex_str = m_PDFParser.clean_latex(tex_str)
        
        #TEMP
        m_PDFParser.render_latex_to_PDF(tex_str, output_filename="C:\\Users\\filip\\Downloads\\output.pdf")