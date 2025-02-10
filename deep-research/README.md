# Domain-Based Deep Research Agent

This Agent is a Deep Research for Domain basis that leverages Composio, agentic frameworks such as LlamaIndex and OpenAI o1 to create a research agent. Ensure you have Python 3.8 or higher installed.


## Steps to Run

1. **Setup Environment**
   ```bash
   # Clone the repository
   git clone https://github.com/TRohit20/LLM-Engineering.git
   cd deep-research

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   Before running the application, you need API keys for the following services:
    - [Get the API key for OpenAI here →](https://platform.openai.com/api-keys)

3. **Run the Setup File**
Make the setup.sh Script Executable (if necessary):
On Linux or macOS, you might need to make the setup.sh script executable:
```shell
chmod +x setup.sh
```
Execute the setup.sh script to set up the environment and install dependencies:
```shell
./setup.sh
```
Now, fill in the `.env` file with your secrets.

4. **Run the Python Script**
```shell
python3 main.py
```

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.