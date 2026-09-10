from pydantic import BaseModel
from typing import List


class ResumeAnalysisResponse(BaseModel):
    skills: List[str]
    skill_count: int
    resume_score: int
    resume_length: int
    status: str