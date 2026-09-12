import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured")

client = OpenAI(api_key=api_key)


def analyze_resume_with_ai(resume_text: str):
    prompt = f"""
You are an expert technical recruiter and resume reviewer.

Analyze the resume below.

Return ONLY valid JSON with exactly these fields:

{{
    "summary": "A concise professional summary",
    "strengths": [
        "strength 1",
        "strength 2",
        "strength 3"
    ],
    "weaknesses": [
        "weakness 1",
        "weakness 2"
    ],
    "technical_skills": [
        "skill 1",
        "skill 2"
    ],
    "improvements": [
        "improvement 1",
        "improvement 2",
        "improvement 3"
    ],
    "career_recommendations": [
        "recommendation 1",
        "recommendation 2"
    ]
}}

Do not include markdown or ```json.

Resume:
{resume_text}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text