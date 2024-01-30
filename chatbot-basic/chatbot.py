import streamlit as st 
from openai import OpenAI
from dotenv import load_dotenv
import os

# Connect OPENAI API KEY to access LLM 
load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

st.title("Your Therapy Friend")

# Initialise chat history 
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to User Input
if prompt := st.chat_input("How are you doing today, friendo?"):
    # Displaying user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role":"user", "content": prompt})

# System respone to the user prompt
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # call the LLM to fetch response to the query 
        for response in client.chat.completions.create(
            model = st.session_state["openai_model"],
            messages = [
                { "role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream = True,
        ):
            # full_response += response.choices[0].delta.get("content", "")
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "  ")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role":"assistant","content": full_response})