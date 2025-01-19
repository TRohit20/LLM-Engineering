
# RAG app to chat with GitHub Repos

This project leverages a python package I recently came across 'GitIngest', which is very handy to parse a GitHub repo in markdown format that can be used as inputs and processing for LLM models.

## Installation and setup

1. **Clone the repository**:
   ```bash
   # Clone the repository
   git clone https://github.com/TRohit20/LLM-Engineering.git
   cd chatwgitrepo-rag
   ```

2. **Install dependencies**:
   Ensure you have Python 3.11 or later running
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   - Get Open AI API key from [OpenAI](https://platform.openai.com/api-keys)

4. Run the Application

    You can run the application using the following command:
    ```bash
    streamlit run local.py
    ```
    Make sure you have Ollama Server running then you can run above command to start the streamlit application.

---

## Contribution

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

## Disclaimer

This tool is for educational and informational purposes only. 