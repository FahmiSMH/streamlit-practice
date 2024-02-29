import streamlit as st
import fileSelector as fs
import checkType as ct
import pdfReader
import prepro as pp
import pattern as pt
from clustering import pca
from foldering import fileClusterDisplay
import pandas as pd
st.title("Project Paperclip")
#maybe time for some changes
def pdfOption(file):
    menu = ['','1 Born PDF','2 Scanned PDF', '3 ScannedByOCR']
    document = []
    option = st.selectbox("Select PDF Properties", menu)
    if st.button("Confirm"):
        match option:
            case '1 Born PDF':
                for f in file: 
                    document.append(pdfReader.pdf2reader(f))
                    #should we save this somewhere?
                    #and iterate it later?
                    #st.write(document)
                    #Ready to delete this when handling multiple files
                st.write("Done Reading")
            case '2 Scanned PDF':
                for f in file: 
                    document.append(pdfReader.ocrReader(f))
                st.write("Done Reading")
            case '3 ScannedByOCR':
                for f in file: 
                    document.append(pdfReader.pdf2reader(f))
                st.write("Done Reading")
        filename=[]
        for d in document:
            string = pp.noSpecial(d)
            token = pp.tokenize(string)
            removed = pp.removeWord(token)
            lemmatized = pp.lemming(removed)
            dataset = pt.toLowerCase(lemmatized)
            finalstring = ' '.join(dataset)
            filename.append(finalstring)
        cluster = pca(filename)
        
        fc = fileClusterDisplay(file, cluster)
        headers = ["Filename","Cluster"]
        df = pd.DataFrame(fc, columns=headers)
        st.table(df)
    return

def sheetOption():
    return

def main():
    file = fs.getEveryFile("data")
    ct.test(file)
    #get every pdf
    file = []
    file = fs.getEveryFile("data/pdf")
    print(file)
    pdfOption(file)
    return
    

if __name__ == "__main__":
    main()