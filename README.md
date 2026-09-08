# 🤖 AI Resume Analyzer API

An intelligent Resume Analyzer API built with **Python and FastAPI** to extract resume content, identify technical skills, and provide structured resume analysis.

---

## 🚀 Features

- 📄 Upload Resume in PDF or TXT format
- 🔍 Extract text from resumes
- 🛠️ Detect technical skills
- 📊 Analyze resume data
- ✅ Resume input validation
- ⚡ Fast REST API using FastAPI
- 📚 Interactive Swagger API documentation
- 🔒 Structured API responses using Pydantic

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| PyPDF | PDF text extraction |
| Pydantic | Data validation & response schemas |
| Git & GitHub | Version control |

---

## 📁 Project Structure

```text
resume-analyzer/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── resume_parser.py
│   └── analyzer.py
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── requirements.txt
├── .gitignore
└── README.md