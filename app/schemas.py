from pydantic import BaseModel
from typing import List


class ResumeAnalysisResponse(BaseModel):
    skills: List[str]
    skill_count: int
    resume_score: int
    strengths: List[str]
    missing_skills: List[str]
    experience_level: str
    word_count: int
    resume_length: int
    status: str


class JobMatchResponse(BaseModel):
    match_score: float
    keyword_score: float
    semantic_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    recommendation: str


class AIResumeAnalysisResponse(BaseModel):
    summary: str
    strengths: List[str]
    weaknesses: List[str]
    technical_skills: List[str]
    improvements: List[str]
    career_recommendations: List[str]