# Realtime Voice Assistant

The AI powered voice assistant app provides a real-time, conversational study abroad consultancy guide for students in India planning to move abroad for their higher education. It transcribes your speech, generates AI responses, and audio synthesis reads out the response with human-like voice. It serves as a professional assistant to help plan your study abroad, providing concise and conversational guidance.

## Features
- Voice synthesis and playback with ElevenLabs.
- Real-time speech-to-text transcription using AssemblyAI.
- AI-generated responses using OpenAI's GPT 4o mini.

## API Key Setup


## How to Run

1. **Setup Environment**
   ```bash
   # Clone the repository
   git clone https://github.com/TRohit20/LLM-Engineering.git
   cd realtime-voice-assistant

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   Before running the application, you need API keys for the following services:

    - [Get the API key for AssemblyAI here →](https://www.assemblyai.com/dashboard/signup)
    - [Get the API key for OpenAI here →](https://platform.openai.com/api-keys)
    - [Get the API key for ElevenLabs here →](https://elevenlabs.io/app/sign-in)

3. **Run the Application**
   ```bash
   python3 realtime-voice-assistant.py
   ```
---

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.