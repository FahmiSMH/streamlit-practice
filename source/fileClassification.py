import os
from PyPDF2 import PdfReader

def reader(filename):

    document = PdfReader(filename)
    document = document.ex
    return document