from langchain.document_loaders import youtube
from openai import OpenAI
import streamlit as st 
import os

from urllib.parse import urlparse, parse_qs
from moviepy.editor import *
from pytube import YouTube
from dotenv import load_dotenv

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI 
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

st.set_page_config(page_title="Y-GPT")
st.header="YOUR YOUTUBE VIDEO URL"
url=st.text_input("Paste/Enter the video url from youtube here")

def download_audio(url: str) -> [str,str]:

    yt = YouTube(url)

    # Extract the video_id from the url
    query = urlparse(url).query
    params = parse_qs(query)
    video_id = params["v"][0]

    # Get the first available audio stream and download it
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path="tmp/")

    # Convert the downloaded audio file to mp3 format
    audio_path = os.path.join("tmp/", audio_stream.default_filename)
    audio_clip = AudioFileClip(audio_path)
    audio_clip.write_audiofile(os.path.join("tmp/", f"{video_id}.mp3"))

    # Delete the original audio stream
    os.remove(audio_path)

    return f"tmp/{video_id}.mp3", video_id

def transcribe_audio(file_path, video_id):
        
        # print("Transcription in process")

        # The path of the transcript
        transcript_filepath = f"tmp/{video_id}.txt"

        # Get the size of the file in bytes
        file_size = os.path.getsize(file_path)

        # Convert bytes to megabytes
        file_size_in_mb = file_size / (1024 * 1024)

        # Check if the file size is less than 25 MB
        if file_size_in_mb < 25:
            with open(file_path, "rb") as audio_file:
                client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
                transcript = client.audio.transcriptions.create(model= "whisper-1",file= audio_file, response_format="text")
                
                # Writing the content of transcript into a txt file
                with open(transcript_filepath, 'w') as transcript_file:
                    transcript_file.write(transcript)

            # Deleting the mp3 file
            os.remove(file_path)
        else:
            print("Please provide a smaller audio file (less than 25mb).")

        # print("exiting transcription function")

@st.cache_data(show_spinner=False)
def generate_summary(url: str) -> str:

    # print("Entered summary function")

    # Define prompt
    prompt_template = """Here is the video transcript:"{docs}"
                    Given above is the transcript of a video. Provide a concise yet comprehensive summary that captures the main points, key discussions, and any notable insights or takeaways.
                    How to perform this task:
                    First, break the transcript into logical sections based on topic or theme. Then, generate a concise summary for each section. Finally, combine these section summaries into an overarching summary of the entire video. The combined summary is what you should return back to me.
                    Things to focus on and include in your final summary:
                    - Ensure to extract the key insights, theories, steps, revelations, opinions, etc discussed in the video. Ensure that the summary provides a clear roadmap for listeners who want to implement the advice or insights(if any) shared.
                    - Identify any controversial or heavily debated points in the video. Summarize the various perspectives presented, ensuring a balanced representation of the video or points in the video.
                    - Along with a content summary, describe the overall mood or tone of the video. Were there moments of tension, humor, or any other notable ambiance details?
                    - Ensure the summary captures all the essense and is in MINIMUM 10 bullet points(can exceed based on the content and aspects)
                    
                    SUMMARY:"""
    prompt = PromptTemplate.from_template(prompt_template)

    # Extract the video_id from the url
    query = urlparse(url).query
    params = parse_qs(query)
    video_id = params["v"][0]

    # The path of the audio file
    audio_path = f"tmp/{video_id}.mp3"

    # The path of the transcript
    transcript_filepath = f"tmp/{video_id}.txt"

    # Check if the transcript file already exist
    if os.path.exists(transcript_filepath):
        # Generating summary of the text file
        with open(transcript_filepath) as f:
            transcript_file = f.read()
    
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_text(transcript_file)
        docs = [Document(page_content=t) for t in texts[:10]]
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,openai_api_key= os.environ.get("OPENAI_API_KEY"))
        # print("llm verified and running")
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="docs")
        # print("summary generated")
        print(stuff_chain.run(docs))
        return stuff_chain.run(docs)
    
    else: 
        download_audio(url)

        # Transcribe the mp3 audio to text
        transcribe_audio(audio_path, video_id)

        # Generating summary of the text file
        with open(transcript_filepath) as f:
            transcript_file = f.read()

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_text(transcript_file)
        docs = [Document(page_content=t) for t in texts[:10]]
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,openai_api_key= os.environ.get("OPENAI_API_KEY"))
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="docs")
        return stuff_chain.run(docs)

if st.button("Submit",type="primary"):
    if url is not None:
        print(url)
        audio_file_path = download_audio(url)
        print(audio_file_path)
        transcribe_audio(audio_file_path[0], audio_file_path[1])
        summary = generate_summary(url=url)
        st.markdown(summary)