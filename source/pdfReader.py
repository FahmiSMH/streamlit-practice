import PyPDF2
# Import the libraries
import pytesseract as pt
import fitz #PymuPDf
import os

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
    file_path = filename  # replace with your file path
    doc = fitz.open(file_path)  # open document

    os.makedirs("images", exist_ok=True)
    for i, page in enumerate(doc):
        pix = page.get_pixmap()  # render page to an image
        image_path = os.path.join("images", f"page_{i}.png")
        pix.save(image_path)  # save image

        text += pt.image_to_string(image_path)
        
    return text

def test():
    file = "dataset/Policy Update.pdf"
    ocrReader(file)
    return

if __name__=="__main__":
    test()