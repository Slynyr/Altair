"""create a class that takes a pdf file and saves first page as a new pdf output"""
import PyPDF2

class PDFProcessor:
    def __init__(self):
        pass
    
    def save_first_page(self, input_pdf):
        with open(input_pdf, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()

            if len(reader.pages) == 0:
                print("PDF is empty")
                return

            first_page = reader.pages[0]
            writer.add_page(first_page)

            with open("out.pdf", 'wb') as output_file:
                writer.write(output_file)

# Usage example
testing = PDFProcessor()
testing.save_first_page("page-1.pdf")
