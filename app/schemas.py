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
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    recommendation: str