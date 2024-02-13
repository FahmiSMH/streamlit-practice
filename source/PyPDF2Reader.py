import PyPDF2

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