# Medical Imaging Analyser

This is a test agent intended to act as a Medical Imaging Analyser using Gemini 2.0 Flash Experimental. The idea is to test the capability of Google's latest model release(The 2.0 model family) WRT images. 
The agent acts as a medical imaging expert analyser to interpret various types of medical images and videos, providing detailed diagnostic insights and explanations.

## Features

- **Image Analysis**
  - Image Type Identification (X-ray, MRI, CT scan, ultrasound)
  - Anatomical Region Detection
  - Key Findings and Observations
  - Potential Abnormalities Detection
  - Image Quality Assessment
  - Research and Reference

## How to Run

1. **Setup Environment**
   ```bash
   # Clone the repository
   git clone https://github.com/TRohit20/LLM-Engineering.git
   cd medical-imaging-analyser

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   - Get Gemini API key from [Google AI Studio](https://aistudio.google.com)

3. **Run the Application**
   ```bash
   streamlit run medical-imaging-analyser.py
   ```

## Analysis Components

- **Image Type and Region**
  - Identifies imaging modality
  - Specifies anatomical region

- **Key Findings**
  - Systematic listing of observations
  - Detailed appearance descriptions
  - Abnormality highlighting

- **Diagnostic Assessment**
  - Potential diagnoses ranking
  - Differential diagnoses
  - Severity assessment

- **Patient-Friendly Explanations**
  - Simplified terminology
  - Detailed first-principles explanations
  - Visual reference points

## Notes

- Uses Gemini 2.0 Flash for analysis
- Requires stable internet connection
- API usage costs apply
- For educational and development purposes only
- Not a replacement for professional medical diagnosis

## Disclaimer

This tool is for educational and informational purposes only. All analyses should be reviewed by qualified healthcare professionals. Do not make medical decisions based solely on this analysis.