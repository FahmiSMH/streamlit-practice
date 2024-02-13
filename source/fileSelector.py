import os
import streamlit as st

def fileSelector(folder_path='.'):
    fileName = os.listdir(folder_path)
    selectedFileName = st.selectbox("Select a file", fileName)
    return os.path.join(folder_path, selectedFileName)

def getEveryFile():
    return

def test():
    return
if __name__ == "__main__":
    test();