from langchain.document_loaders import youtube
from openai import OpenAI
import streamlit as st 
import os

from urllib.parse import urlparse, parse_qs
from moviepy.editor import *
from pytube import YouTube
from dotenv import load_dotenv

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

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

@st.cache_data(show_spinner=False)
def generate_answer(url: str, question: str) -> str:

    print("Entered Answer gen function")

    # Define the prompt
    prompt = """{context}

    Use the above pieces of context to answer the following question: {question}
    If you don't know the answer, just say that you don't know or verify and tell that the video does not cover about it, don't try to make up an answer.
    Use two sentences minimum and keep the answer as concise and comprehensive as possible.
    Always say "thanks for asking!" at the end of the answer.

    Helpful Answer:
    """
    custom_prompt = PromptTemplate.from_template(prompt)

    print("Prompt passed")

    # Extract the video_id from the url
    query = urlparse(url).query
    params = parse_qs(query)
    video_id = params["v"][0]

    # The path of the audio file
    audio_path = f"tmp/{video_id}.mp3"

    # The path of the transcript
    transcript_filepath = f"tmp/{video_id}.txt"

    if os.path.exists(transcript_filepath):
        # Generating summary of the text file
        with open(transcript_filepath) as f:
            transcript_file = f.read()

        loader = TextLoader(transcript_filepath, encoding="utf8")
        docs = loader.load()
        llm = ChatOpenAI(temperature=0,openai_api_key= os.environ.get("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-1106")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        print("LLM verified and Docs stored in VBD")
        
        # Retrieve and generate using the relevant snippets of the video
        vectorstore = chroma.Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(api_key=os.environ.get("OPENAI_API_KEY")))
        retriever = vectorstore.as_retriever()
        print("retriever job done")
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)


        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | custom_prompt
            | llm
            | StrOutputParser()
        )

        print(rag_chain.invoke(question))
        return rag_chain.invoke(question)
    
    else: 
        download_audio(url)

        # Transcribe the mp3 audio to text
        transcribe_audio(audio_path, video_id)

        loader = TextLoader(transcript_filepath, encoding="utf8")
        docs = loader.load()
        llm = ChatOpenAI(temperature=0,openai_api_key= os.environ.get("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-1106")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        
        # Retrieve and generate using the relevant snippets of the video
        vectorstore = chroma.Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(api_key=os.environ.get("OPENAI_API_KEY")))
        retriever = vectorstore.as_retriever()
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)


        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | custom_prompt
            | llm
            | StrOutputParser()
        )

        return rag_chain.invoke(question)