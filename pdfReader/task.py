import base64
import io
import PyPDF2
import os
import sys

def get_required_Data(encoded_data, page_num):
    decoded = base64.b64decode(encoded_data)
    pdf_file = io.BytesIO(decoded)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    if page_num < 0 or page_num >= len(pdf_reader.pages):
        return None, "Invalid page number, please choose valid page number"
    else:   
        page = pdf_reader.pages[page_num]
        print("---Thank you!---") 
        return page, None

def required_page(page_data, name):
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page_data)
    with open(name, 'wb') as f:
         pdf_writer.write(f)
         
def pdf_encode(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf_bin = f.read()
        pdf_encode = base64.b64encode(pdf_bin).decode('utf-8')
    return pdf_encode

if __name__ == "__main__":
    
    pdf_path = sys.argv[1]
    page_num = int(sys.argv[2])
    pdf_encode_str = pdf_encode(pdf_path)
    
    
    page_data, error_message = get_required_Data(pdf_encode_str, page_num)
    if page_data:
        # Save the page as 'decoded.pdf'
        required_page(page_data, 'decoded.pdf')
        print("Page has been saved as 'decoded.pdf'")
    else:
        print(error_message)
