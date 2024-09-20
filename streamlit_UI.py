from PyPDF2 import PdfReader # type: ignore
import streamlit as st # type: ignore
import io
import time

def dummy_operation(pdf):
    time.sleep(5)
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    return text

st.header("CV Generation", divider='rainbow')

# input part
user_text = st.text_area("Enter some text:")
uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf"])

if st.button("Generate CV"):
    if uploaded_file:
        with st.spinner('Processing CV, Hacking nasa...'):
            processed_content = dummy_operation(uploaded_file) + user_text

        st.download_button(
            label="Download Processed File",
            data=processed_content,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
        st.success("Done!")
    else:
        st.error("Please upload a file to process.")
