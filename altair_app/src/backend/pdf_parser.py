"""create a class that takes a pdf file and saves first page as a new pdf output"""
import PyPDF2
import io
import base64

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
        return first_page
