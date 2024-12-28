## Chat with Research Papers from Arxiv
This is a simple app built using streamlit framework enables you to chat with arXiv, a vast repository of scholarly articles, using LLMs. 
The app is built with the intention to make reading and learning from research papers easy and accessible. 
The app can break down the research paper into simple explanations and answer questions regarding specific parts of the paper(with ArXivToolKit doing a lot of the heavy lifting in the background, thank you, Phidata)

### Features
- Access and explore a vast collection of research papers
- Chat and interact with research papers in simple, yet useful manner
- Utilize OpenAI or Llama for intelligent responses

### How to get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/TRohit20/LLM-Engineering.git
cd ChatwPapers-RAG
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Get your OpenAI API Key

- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.

In case of Llama 3.2, you donot need to do anything much.

4. Run the Streamlit App
```bash
streamlit run app.py/Llama_app.py
```