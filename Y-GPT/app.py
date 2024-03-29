from langchain.document_loaders import youtube
import streamlit as st 
from brain import generate_summary, generate_answer, generate_summary_for_brightcove, generate_answer_for_brightcove

with st.sidebar:
    st.markdown("### 🎥 Y-GPT: Your Shortcut to Video Insights")

    st.markdown("## What's Y-GPT ?")
    st.markdown("""<div style="text-align: justify;">Have you ever wanted just the gist and key takeaways from a video or found yourself going through a long YouTube video, trying to find the answer to a specific question? With GPTube, 
                    you can simply ask the question you want to find the answer to, and in less than 5 minutes, 
                    you can get the answer.<br></div>""", unsafe_allow_html=True)
        
st.markdown('## 🎬 Talk with Videos') 

choice = st.radio("Please choose an option :", ('Generate Summary', 'Generate Answer to a Question', 'Brightcove Video', 'Brightcove Q&A'), horizontal=True)

st.markdown('#### 📼 Step 1 : Enter a Video URL')
url = st.text_input("URL :", placeholder="https://www.youtube.com/watch?v=************")

if choice == "Generate Summary":
    if st.button("Generate Summary"):
        with st.spinner("Generating summary."):
            summary = generate_summary(url=url)
        st.markdown(f"📃 Video Summary:")
        st.success(summary)
elif choice == "Generate Answer to a Question":
    if st.button("Generate Summary"):
        with st.spinner("Generating summary."):
            summary = generate_summary(url=url)
        st.markdown(f"📃 Video Summary:")
        st.success(summary)
    st.markdown('🤔 Step 2 : Enter your question')
    question = st.text_input("Ask something you wanna know from the video?", placeholder="Ask something you wanna know from the video?")
    if st.button("Generate Answer"):
        with st.spinner("Generating answer:"):
            answer = generate_answer(url=url, question=question)
        st.markdown(f"🤖 {question}")
        st.success(answer)
elif choice == "Brightcove Video":
    if st.button("Summary"):
        with st.spinner("Retrieving Video and Generating Summary"):
            summary = generate_summary_for_brightcove(url=url)
        st.markdown(f"📃 Video Summary:")
        st.success(summary)
elif choice == "Brightcove Q&A":
    if st.button("Summary"):
        with st.spinner("Retrieving Brightcove Video Summary..."):
            summary = generate_summary_for_brightcove(url=url)
        st.markdown(f"Video Summary:")
        st.success(summary)
    st.markdown('🤔 Step 2 : Enter your question')
    question = st.text_input("Ask something you wanna know from the video?", placeholder="Ask something you wanna know from the video?")
    if st.button("Answer"):
        with st.spinner("Fetching and streamlining answer to the question"):
            answer = generate_answer_for_brightcove(url=url, question=question)
        st.markdown(f"🤖 {question}")
        st.success(answer)

# Hide Left Menu
st.markdown("""<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>""", unsafe_allow_html=True)