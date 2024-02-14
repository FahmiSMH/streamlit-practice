import streamlit as st
import fileSelector as fs
import pdfReader

st.title("Project Paperclip")
#maybe time for some changes
def folderSelection():
    st.write("Browse for dataset folder")
    return

def main():
    file = "dataset/Policy Update.pdf"
    menu = ['','1 Born PDF','2 Scanned PDF', '3 ScannedByOCR']
    option = st.selectbox("Select PDF Properties", menu)
    if st.button("Confirm"):
        match option:
            case '1 Born PDF':
                document = pdfReader.pdf2reader(file)
                #Ready to delete this when handling multiple files
                st.write(document)
            case '2 Scanned PDF':
                document = pdfReader.ocrReader(file)
                st.write(document)
            case '3 ScannedbyOCR':
                document = pdfReader.pdf2reader(file)
                st.write(document)
    return

if __name__ == "__main__":
    main()