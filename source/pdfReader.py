import PyPDF2
# Import the libraries
import pytesseract
import pdf2image
from PIL import Image

def pdf2reader(filename):
    #initialize
    longtext = ""
    reader = PyPDF2.PdfReader(filename)

    #see how many pages in the document
    #print(len(reader.pages))
    
    #append to a string, the content of the pages
    for r in reader.pages:
        longtext += r.extract_text()

    return longtext

def ocrReader(filename):
    # Specify the path to the PDF file
    pdf_file = "sample.pdf"
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages

    # Loop through each page
    for page in range(num_pages):

        pdf_page = pdf_reader.getPage(page)
        pdf_image = pdf2image.convert_from_bytes(pdf_page.extractBytes())[0]
        pdf_image.save(f"page_{page}.png")
        image = Image.open(f"page_{page}.png")
        text = pytesseract.image_to_string(image)
        print(text)
        with open("output.txt", "a") as f:
            f.write(text + "\n")
    return text