"""create a class that takes a pdf file and saves first page as a new pdf output"""
import PyPDF2
import io
import base64

#create class for parsing pdf
class PDFParser:
    def __init__(self):
        pass
    
    
    def get_page_data(self, file_path):
        with open(file_path, 'rb') as pdf_file: #opens pdf file, creating a reader and writer
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()

            if len(reader.pages) == 0: #returns if there is no pdf
                print("PDF is empty")
                return []
            
            output_data = [] #empty list to store base64 based string which represents each page
            
            for i in range(0, len(reader.pages)): #creates a new pdf write for each page and adds page to the writer
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[i])

                output_stream = io.BytesIO() #stores the pdf
                writer.write(output_stream) 
                output_stream.seek(0) #stream position is reset

                base64_encoded = base64.b64encode(output_stream.getvalue()).decode('utf-8')
                output_data.append(base64_encoded)
        return output_data
