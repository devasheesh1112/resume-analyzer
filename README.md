# AI Resume Analyzer

AI-powered Resume Analysis API built with FastAPI and OpenAI.

## Features
- PDF/TXT resume parsing
- Technical skill extraction
- Resume scoring
- Strength & weakness analysis
- Missing skill detection
- Experience-level detection
- Job description matching
- AI-powered resume analysis
- Structured JSON responses
- Input validation and error handling

## Tech Stack
- Python
- FastAPI
- Pydantic
- OpenAI API
- PyPDF
- Pytest

## API Endpoints

### GET /
Health check

### POST /analyze-resume
Analyzes resume and returns:
- skills
- resume score
- strengths
- missing skills
- experience level
- word count

### POST /match-job
Compares resume against a job description and returns:
- match score
- matched skills
- missing skills
- recommendation

### POST /ai-analyze-resume
Uses OpenAI to generate:
- professional summary
- strengths
- weaknesses
- technical skills
- improvements
- career recommendations

## Project Structure

resume-analyzer/
├── app/
│   ├── main.py
│   ├── analyzer.py
│   ├── ai_analyzer.py
│   ├── resume_parser.py
│   └── schemas.py
├── tests/
├── requirements.txt
├── .env
└── README.md

## Setup

git clone https://github.com/devasheesh1112/resume-analyzer.git

cd resume-analyzer

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

## Environment Variables

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here

Never commit your `.env` file.

## Run

python -m uvicorn app.main:app --reload

API documentation:

http://127.0.0.1:8000/docs

## Example AI Response

{
  "summary": "Backend-focused software engineer...",
  "strengths": [
    "Strong Python knowledge",
    "Backend development experience"
  ],
  "weaknesses": [
    "Limited cloud exposure"
  ],
  "technical_skills": [
    "Python",
    "FastAPI",
    "PostgreSQL"
  ],
  "improvements": [
    "Add measurable project achievements"
  ],
  "career_recommendations": [
    "Backend Software Engineer",
    "Python Developer"
  ]
}

## Future Improvements

- Semantic resume-job matching
- Embedding-based similarity
- Database integration
- Authentication
- Resume history
- Async AI processing
- Docker deployment
- Cloud deployment

## Author

Devasheesh Patidar

GitHub: https://github.com/devasheesh1112
LinkedIn: https://www.linkedin.com/in/devasheesh-patidar