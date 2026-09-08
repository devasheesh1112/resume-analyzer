from fastapi import FastAPI, UploadFile, File
from app.resume_parser import extract_text
from app.analyzer import analyze_resume

app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered Resume Analysis API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.post("/analyze-resume")
async def analyze_resume_api(file: UploadFile = File(...)):

    content = await file.read()

    resume_text = extract_text(
        content,
        file.filename
    )

    result = analyze_resume(resume_text)

    return result