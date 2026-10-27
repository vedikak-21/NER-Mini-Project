# Named Entity Recognition System Using Natural Language Processing

## Project Overview
This project is a Named Entity Recognition (NER) system built using Python, spaCy, Streamlit, and Pandas. The application allows users to enter text or upload a `.txt` file and detect named entities such as persons, organizations, locations, dates, money, and other categories supported by the spaCy English model.

The system is designed to be simple, interactive, and easy to understand for academic and portfolio use. It provides both visual and tabular outputs for better interpretation of the extracted named entities.

## Abstract
Named Entity Recognition (NER) is a fundamental task in Natural Language Processing (NLP) that aims to identify and classify meaningful entities in text, such as names of people, organizations, locations, dates, and monetary values. This project focuses on building an interactive NER system using the spaCy library and a Streamlit user interface.

The application accepts input text from the user and processes it using a pretrained English language model. It then extracts named entities, highlights them in the original text, and displays the detected entities in a tabular format. The project demonstrates the practical use of NLP for information extraction and data analysis in a beginner-friendly and accessible way.

## Problem Statement
In large amounts of unstructured text, it is often difficult to quickly identify important information such as people, organizations, locations, dates, and monetary values. Manual extraction is time-consuming and error-prone. There is a need for an efficient automated method to identify and classify these entities accurately.

## Objectives
- To build an interactive Named Entity Recognition application.
- To process user input and uploaded text files efficiently.
- To use spaCy's pretrained NLP pipeline for entity recognition.
- To display recognized entities with labels and positions.
- To visualize and summarize the extracted results.
- To provide a simple project suitable for academic demonstration and portfolio presentation.

## Features
- Text input for direct analysis
- Upload support for `.txt` files
- Entity extraction using spaCy
- Highlighting of recognized entities in the original text
- Entity table with labels and positions
- Total count and unique entity count metrics
- Bar chart for entity type distribution
- CSV download of results
- User-friendly interface built with Streamlit

## Technologies Used
- Python
- Streamlit
- spaCy
- Pandas
- Natural Language Processing (NLP)

## Project Folder Structure
```text
NER-Mini-Project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── venv/                  # Local virtual environment (not uploaded to GitHub)
├── __pycache__/          # Python cache files (ignored by Git)
└── .vscode/              # Editor settings (ignored by Git when appropriate)
```

## Installation Instructions for Windows

### 1. Open PowerShell in the project folder
```powershell
cd C:\Users\vedik\NER-Mini-Project
```

### 2. Create a virtual environment
```powershell
py -m venv venv
```

### 3. Activate the virtual environment
```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Upgrade pip
```powershell
python -m pip install --upgrade pip
```

### 5. Install dependencies
```powershell
pip install -r requirements.txt
```

### 6. Install the spaCy English model
```powershell
python -m spacy download en_core_web_sm
```

## Running the Application Locally
```powershell
python -m streamlit run app.py
```

The app will open in the browser, usually at:

```text
http://localhost:8501
```

## Example Input
```text
Sundar Pichai is the CEO of Google. He visited Mumbai on 15 October 2026 and announced an investment of 500 million dollars.
```

## Example Expected Output
The application may detect entities such as:

- `Sundar Pichai` → PERSON
- `Google` → ORG
- `Mumbai` → GPE
- `15 October 2026` → DATE
- `500 million dollars` → MONEY

The exact results depend on the pretrained spaCy model and the text provided.

## Applications of NER
Named Entity Recognition is used in many real-world domains, including:
- News analysis and summarization
- Customer support automation
- Search engine result enhancement
- Healthcare record processing
- Financial document analysis
- Social media monitoring
- Email classification and categorization

## Limitations
- The system uses a pretrained spaCy model rather than a custom-trained model.
- Performance may vary depending on the text quality and context.
- Some entity categories may not be detected accurately in informal or noisy text.
- The project is designed for demonstration and academic use rather than large-scale deployment.

## Future Enhancements
- Train a custom NER model on a domain-specific dataset.
- Add support for multiple languages.
- Improve visualization and entity highlighting.
- Add evaluation metrics such as precision, recall, and F1-score.
- Integrate with a database or web API.
- Deploy on Streamlit Community Cloud or a cloud-hosted web platform.

## Deployment Preparation
This project is structured to be deployable with Streamlit Community Cloud. The main application file is `app.py`, and the required dependencies are listed in `requirements.txt`.

Use the following command to run it locally:

```powershell
python -m streamlit run app.py
```

## GitHub Project Note
This project is intended for academic demonstration and portfolio presentation. It should be uploaded to GitHub with only the required source files and not with the local virtual environment or secret credentials.
