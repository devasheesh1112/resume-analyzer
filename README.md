# AI Resume Analyzer API

AI-powered Resume Analyzer API built with FastAPI and Python.

## Features

- Upload Resume (PDF/Text)
- Extract Resume Content
- Detect Technical Skills
- Analyze Resume Data
- REST API with FastAPI
- Interactive Swagger Documentation

## Tech Stack

- Python
- FastAPI
- Uvicorn
- PyPDF
- Pydantic

## Project Structure

```text
resume-analyzer/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── resume_parser.py
│   └── analyzer.py
│
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
git clone https://github.com/devasheesh1112/resume-analyzer.git

cd resume-analyzer

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Run Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

### Analyze Resume

```http
POST /analyze-resume
```

Upload a PDF resume and receive analysis results.

## Future Improvements

- AI-based Resume Analysis
- Job Description Matching
- Resume Score Calculation
- PostgreSQL Integration
- Docker Support
- CI/CD Pipeline
- GitHub Actions

## Author

Devasheesh Patidar
