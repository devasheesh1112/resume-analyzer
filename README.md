# 🤖 AI Resume Analyzer

An AI-powered Resume Analysis API built with **FastAPI, Python, Sentence Transformers, and OpenAI**.

The system analyzes resumes, extracts technical skills, scores resume quality, compares resumes with job descriptions, and provides AI-powered career feedback.

---

## 🚀 Features

### 📄 Resume Analysis
- PDF and TXT resume parsing
- Technical skill extraction
- Resume quality score
- Strength detection
- Missing skill detection
- Experience-level classification
- Word count analysis

### 🎯 Job Description Matching
- Keyword-based skill matching
- Semantic similarity matching
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

### 🛡️ API Validation
- File type validation
- Empty file validation
- Resume content validation
- Structured Pydantic responses
- Error handling

---

## 🏗️ Architecture

```text
                    Resume
                       │
                       ▼
                ┌──────────────┐
                │ FastAPI API  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Resume Parser│
                └──────┬───────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Rule-Based     Semantic       OpenAI
      Analysis      Matching       Analysis
          │            │            │
          ▼            ▼            ▼
      Resume       Job Match     AI Insights
       Score          Score
          │            │            │
          └────────────┼────────────┘
                       ▼
                 JSON Response