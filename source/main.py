import streamlit as st
import fileSelector as fs
import checkType as ct
import pdfReader

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
                document = pdfReader.ocrReader(file)
                st.write(document)
            case '3 ScannedByOCR':
                document = pdfReader.pdf2reader(file)
                st.write(document)
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