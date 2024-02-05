from langchain.document_loaders import youtube
import streamlit as st 

from brain import download_audio, transcribe_audio, generate_summary

st.set_page_config(page_title="Y-GPT")
st.header="YOUR YOUTUBE VIDEO URL"
url=st.text_input("Paste/Enter the video url from youtube here")

if st.button("Submit",type="primary"):
    if url is not None:
        print(url)
        audio_file_path = download_audio(url)
        print(audio_file_path)
        transcribe_audio(audio_file_path[0], audio_file_path[1])
        summary = generate_summary(url=url)
        st.markdown(summary)