from fastapi import FastAPI, UploadFile, File, HTTPException
from app.analyzer import analyze_resume, match_resume_with_job

from app.resume_parser import extract_text
from app.analyzer import analyze_resume
from app.schemas import ResumeAnalysisResponse
from app.schemas import ResumeAnalysisResponse, JobMatchResponse

app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered Resume Analysis API",
    version="2.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running",
        "version": "2.0.0"
    }


@app.post(
    "/analyze-resume",
    response_model=ResumeAnalysisResponse
)
async def analyze_resume_api(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required"
        )

    allowed_extensions = (".pdf", ".txt")

    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported"
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty"
        )

    try:
        resume_text = extract_text(content, file.filename)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to extract text from the uploaded file"
        )

    if not resume_text:
        raise HTTPException(
            status_code=400,
            detail="No readable text found in the resume"
        )

    # Validate minimum resume content
    if len(resume_text.strip()) < 50:
        raise HTTPException(
            status_code=400,
            detail="Resume content is too short to analyze"
        )

    result = analyze_resume(resume_text)

    return result


@app.post(
    "/match-job",
    response_model=JobMatchResponse
)
async def match_job(
    file: UploadFile = File(...),
    job_description: str = ""
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required"
        )

    allowed_extensions = (".pdf", ".txt")

    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported"
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description is required"
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty"
        )

    try:
        resume_text = extract_text(content, file.filename)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to extract text from the uploaded file"
        )

    if not resume_text:
        raise HTTPException(
            status_code=400,
            detail="No readable text found in the resume"
        )

    result = match_resume_with_job(
        resume_text,
        job_description
    )

    return result