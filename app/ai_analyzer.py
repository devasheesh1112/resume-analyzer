import json
import os

from dotenv import load_dotenv
from openai import OpenAI


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

Rules:
- Return only JSON.
- Do not use markdown.
- Do not include ```json.
- Keep the analysis concise and professional.
- Base the analysis only on the resume content.

Resume:

{resume_text}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    output = response.output_text.strip()

    try:
        result = json.loads(output)
    except json.JSONDecodeError as e:
        raise ValueError(
            "AI returned an invalid JSON response"
        ) from e

    required_fields = [
        "summary",
        "strengths",
        "weaknesses",
        "technical_skills",
        "improvements",
        "career_recommendations"
    ]

    for field in required_fields:
        if field not in result:
            raise ValueError(
                f"AI response is missing required field: {field}"
            )

    return result