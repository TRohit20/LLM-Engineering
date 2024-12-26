# Local AI Chat Assistant 
This PoC leverages Llama 3.2 vision and Chainlit to create a 100% locally running AI chat assistant more like ChatGPT app.
The idea is to run the AI chat app entirely local, this way, your data is always safe and private

## Installation and setup

**Setup Ollama**:
   ```bash
   # setup ollama on linux 
   curl -fsSL https://ollama.com/install.sh | sh
   # pull llama 3.2 vision model
   ollama pull llama3.2-vision 
   ```


**Install Dependencies**:
   Ensure you have Python 3.11 or later installed.
   ```bash
   pip install -r requirements.txt
   ```

**Run the app**:
   Run the chainlit app as follows:
   ```bash
   chainlit run app.py -w
   ```

---