import streamlit as st
import fileSelector as fs

st.title("Project Paperclip")

fileName = fs.fileSelector()

st.write("you selected '%s' " %fileName)
#maybe time for some changes