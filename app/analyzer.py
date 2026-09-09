def analyze_resume(resume_text: str):

    skills_database = [
    "Python",
    "Django",
    "FastAPI",
    "Flask",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "Redis",
    "Docker",
    "Kubernetes",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "AWS",
    "Git",
    "Java",
    "C++",
    "JavaScript",
    "React",
    "Node.js",
    "SQL",
    "REST API",
    "Microservices"
]

    found_skills = []

    resume_lower = resume_text.lower()

    for skill in skills_database:
        if skill.lower() in resume_lower:
            found_skills.append(skill)

    return {
        "skills": found_skills,
        "skill_count": len(found_skills),
        "resume_length": len(resume_text),
        "status": "Resume analyzed successfully"
    }