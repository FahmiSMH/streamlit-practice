import os
import streamlit as st

def fileSelector(folder_path='.'):
    fileName = os.listdir(folder_path)
    selectedFileName = st.selectbox("Select a file", fileName)
    return os.path.join(folder_path, selectedFileName)

def getEveryFile(dataset):
    filelist=[]
    for root, dirs, files in os.walk(dataset):
        for file in files:
                filename=os.path.join(root, file)
                filelist.append(filename)   
    return filelist

def test():
    dataset = getEveryFile()
    st.write(dataset)
    return
if __name__ == "__main__":
    test();