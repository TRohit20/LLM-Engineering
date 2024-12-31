# Personalised Cold Email Writer 

The **Cold Email Writer** is an intelligent agent designed to fetch job details from postings and generate personalized cold emails to hiring teams, leveraging a matched talent pool. This project utilizes advanced AI models to streamline the recruitment process.

## Features

- **Job Description Parsing**: Automatically extracts key components from job postings.
- **Cold Email Generation**: Creates personalized cold emails based on job descriptions and candidate profiles.
- **Web Scraping**: Fetches job details from specified URLs.
- **Rich Output**: Generates well-structured emails that highlight relevant skills and experiences.

## How to Run

Follow these steps to set up and run the Cold Email Writer application.

### Setup Environment

1. **Clone the repository**:
   ```bash
   # Clone the repository
   git clone https://github.com/TRohit20/LLM-Engineering.git
   cd cold-email-writer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   - Get Grok AI API key from [Groq AI](https://console.groq.com/keys)

4. Run the Application

    You can run the application using the following command:
    ```bash
    python app.py
    ```
    This will start a Gradio interface where you can input job posting URLs and receive generated cold emails.

## Project Structure

```
cold-email-writer/
│
├── app.py                     # Main application file
├── config.py                  # Configuration management
├── agent/                     # Contains agent logic for email writing and job description parsing
│   ├── cold_email_writer_agent/
│   │   ├── agent.py           # Cold email writer agent logic
│   │   └── model.py           # Data models for cold email writing
│   └── jd_parser_agent/
│       ├── agent.py           # Job description parser agent logic
│       └── model.py           # Data models for job description parsing
├── utils.py                   # Utility functions for web scraping and text processing
└── requirements.txt           # Python dependencies
```

## Usage

1. **Input Job Posting URL**: Enter the URL of the job posting in the provided textbox in the Gradio interface.
2. **Generate Cold Email**: Click the button to generate a cold email based on the job description fetched from the URL.
3. **Review Output**: The generated email will be displayed in the output textbox.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

## Disclaimer

This tool is for educational and informational purposes only. 