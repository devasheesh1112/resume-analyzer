# 🤖 AI Resume Analyzer

An AI-powered Resume Analysis API built with **FastAPI, Python, Sentence Transformers, and OpenAI**.

The system analyzes resumes, extracts technical skills, evaluates resume quality, compares resumes with job descriptions using **hybrid keyword + semantic matching**, and provides AI-powered career feedback.

---

## 🚀 Features

### 📄 Resume Analysis

- PDF and TXT resume parsing
- Technical skill extraction
- Resume quality scoring
- Strength detection
- Missing skill detection
- Experience-level classification
- Word count analysis
- Resume content validation

### 🎯 Job Description Matching

- Keyword-based skill matching
- Semantic similarity using Sentence Transformers
- Hybrid job matching score
- Matched skills detection
- Missing skills detection
- Job application recommendation

### 🧠 AI Resume Analysis

- AI-generated professional summary
- Strength analysis
- Weakness analysis
- Technical skill identification
- Resume improvement suggestions
- Career recommendations
- Structured JSON AI responses

### 🛡️ API Validation

- File type validation
- Empty file validation
- Resume content validation
- Pydantic response models
- HTTP error handling
- Structured API responses

---

## 🏗️ Architecture

```text
                         Resume
                            │
                            ▼
                    ┌──────────────┐
                    │  FastAPI API │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ Resume Parser│
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        Rule-Based      Semantic       OpenAI
         Analysis       Matching       Analysis
              │            │            │
              ▼            ▼            ▼
        Resume Score    Job Match     AI Insights
        Skill Analysis    Score
              │            │            │
              └────────────┼────────────┘
                           ▼
                     JSON Response






Upload Resume
      │
      ▼
Validate File
      │
      ▼
Extract Resume Text
      │
      ▼
Resume Analysis
      │
      ├──► Skill Extraction
      ├──► Resume Scoring
      ├──► Experience Classification
      └──► Missing Skill Detection
      │
      ▼
Job Matching
      │
      ├──► Keyword Matching
      └──► Semantic Matching
      │
      ▼
AI Analysis
      │
      ├──► Summary
      ├──► Strengths
      ├──► Weaknesses
      └──► Recommendations
      │
      ▼
Structured JSON Response







Resume
  │
  ├──► Keyword Matching ──────► Keyword Score (40%)
  │
  └──► Semantic Matching ─────► Semantic Score (60%)
                                      │
                                      ▼
                              Final Match Score





Final Score =
    (Keyword Score × 0.40)
  + (Semantic Score × 0.60)






Resume Text
     │
     ▼
Sentence Transformer
     │
     ▼
Resume Embedding
     │
     ├──────────────► Cosine Similarity
     │
     ▼
Job Description Embedding
     │
     ▼
Semantic Score




resume-analyzer/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── analyzer.py
│   ├── ai_analyzer.py
│   ├── semantic_matcher.py
│   ├── resume_parser.py
│   └── schemas.py
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── requirements.txt
├── .gitignore
└── README.md

ssssss
Name owner :
Devasheesh Patidar