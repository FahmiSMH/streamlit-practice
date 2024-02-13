import streamlit as st
import fileSelector as fs

st.title("Project Paperclip")
#maybe time for some changes
def main():
    
    menu = ['','1 Born PDF','2 Scanned PDF', '3 ScannedByOCR']
    option = st.selectbox("Select PDF Properties", menu)
    if st.button("Confirm"):
        match option:
            case '1 Born PDF':
                st.write("what")
    return

if __name__ == "__main__":
    main()