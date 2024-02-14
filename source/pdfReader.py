import PyPDF2
# Import the libraries
import pytesseract as pt
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
    text=""
    ocrReader = PyPDF2.PdfReader(filename)
    images = pdf2image.pdfinfo_from_path(filename)
 
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')

    for i in images:
        text += pt.image_to_string(i)
        print("text")
    return text

def test():
    file = "dataset/Policy Update.pdf"
    ocrReader(file)
    return

if __name__=="__main__":
    test()