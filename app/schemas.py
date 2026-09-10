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

    resume_lower = resume_text.lower()

    # Detect technical skills
    found_skills = []

    for skill in skills_database:
        if skill.lower() in resume_lower:
            found_skills.append(skill)

    # -----------------------------
    # Resume Score Calculation
    # -----------------------------

    score = 0

    # 1. Technical skills - 40 points
    skill_score = min(len(found_skills) * 3, 40)
    score += skill_score

    # 2. Resume content length - 20 points
    word_count = len(resume_text.split())

    if word_count >= 500:
        score += 20
    elif word_count >= 300:
        score += 15
    elif word_count >= 150:
        score += 10
    elif word_count >= 75:
        score += 5

    # 3. Projects / Experience - 20 points
    experience_keywords = [
        "experience",
        "work experience",
        "employment",
        "internship",
        "project",
        "projects"
    ]

    experience_matches = sum(
        1 for keyword in experience_keywords
        if keyword in resume_lower
    )

    score += min(experience_matches * 4, 20)

    # 4. Education - 10 points
    education_keywords = [
        "education",
        "bachelor",
        "master",
        "b.tech",
        "m.tech",
        "degree",
        "university",
        "college"
    ]

    education_matches = sum(
        1 for keyword in education_keywords
        if keyword in resume_lower
    )

    if education_matches >= 2:
        score += 10
    elif education_matches == 1:
        score += 5

    # 5. Contact information - 10 points
    contact_score = 0

    if "@" in resume_text:
        contact_score += 5

    if any(char.isdigit() for char in resume_text):
        contact_score += 5

    score += contact_score

    # Make sure score stays between 0 and 100
    score = min(score, 100)

    return {
        "skills": found_skills,
        "skill_count": len(found_skills),
        "resume_score": score,
        "resume_length": len(resume_text),
        "status": "Resume analyzed successfully"
    }