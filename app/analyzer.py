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

    # -----------------------------
    # Skill Detection
    # -----------------------------

    found_skills = []

    for skill in skills_database:
        if skill.lower() in resume_lower:
            found_skills.append(skill)

    # -----------------------------
    # Resume Score
    # -----------------------------

    score = 0

    # Technical skills - 40 points
    skill_score = min(len(found_skills) * 3, 40)
    score += skill_score

    # Resume content - 20 points
    word_count = len(resume_text.split())

    if word_count >= 500:
        score += 20
    elif word_count >= 300:
        score += 15
    elif word_count >= 150:
        score += 10
    elif word_count >= 75:
        score += 5

    # Experience / Projects - 20 points
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

    # Education - 10 points
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

    # Contact information - 10 points
    if "@" in resume_text:
        score += 5

    if any(char.isdigit() for char in resume_text):
        score += 5

    score = min(score, 100)

    # -----------------------------
    # Missing Skills
    # -----------------------------

    recommended_skills = [
        "Python",
        "SQL",
        "Git",
        "REST API",
        "Docker",
        "PostgreSQL",
        "Redis",
        "AWS",
        "Kubernetes",
        "Microservices"
    ]

    missing_skills = [
        skill
        for skill in recommended_skills
        if skill.lower() not in resume_lower
    ]

    # -----------------------------
    # Strengths
    # -----------------------------

    strengths = []

    if len(found_skills) >= 5:
        strengths.append("Strong technical skill set")
    elif len(found_skills) >= 3:
        strengths.append("Good technical skill set")

    if any(
        keyword in resume_lower
        for keyword in ["fastapi", "django", "flask", "rest api"]
    ):
        strengths.append("Backend development exposure")

    if any(
        keyword in resume_lower
        for keyword in ["postgresql", "mysql", "mongodb", "sql"]
    ):
        strengths.append("Database knowledge")

    if any(
        keyword in resume_lower
        for keyword in ["project", "projects"]
    ):
        strengths.append("Project experience")

    if any(
        keyword in resume_lower
        for keyword in ["docker", "kubernetes", "aws"]
    ):
        strengths.append("Cloud and DevOps exposure")

    if not strengths:
        strengths.append("Resume has basic professional information")

    # -----------------------------
    # Experience Level
    # -----------------------------

    if any(
        keyword in resume_lower
        for keyword in [
            "senior",
            "lead developer",
            "tech lead",
            "principal engineer"
        ]
    ):
        experience_level = "Senior Level"

    elif any(
        keyword in resume_lower
        for keyword in [
            "2 years",
            "3 years",
            "4 years",
            "5 years",
            "experience"
        ]
    ):
        experience_level = "Mid Level"

    elif any(
        keyword in resume_lower
        for keyword in [
            "intern",
            "internship",
            "fresher",
            "entry level"
        ]
    ):
        experience_level = "Entry Level"

    else:
        experience_level = "Entry Level"

    return {
        "skills": found_skills,
        "skill_count": len(found_skills),
        "resume_score": score,
        "strengths": strengths,
        "missing_skills": missing_skills,
        "experience_level": experience_level,
        "word_count": word_count,
        "resume_length": len(resume_text),
        "status": "Resume analyzed successfully"
    }


def match_resume_with_job(resume_text: str, job_description: str):
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
    job_lower = job_description.lower()

    # Skills required by the job
    job_skills = [
        skill
        for skill in skills_database
        if skill.lower() in job_lower
    ]

    # Skills present in the resume
    resume_skills = [
        skill
        for skill in skills_database
        if skill.lower() in resume_lower
    ]

    # Skills present in both
    matched_skills = [
        skill
        for skill in job_skills
        if skill in resume_skills
    ]

    # Required skills missing from resume
    missing_skills = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]

    # Calculate match score
    if not job_skills:
        match_score = 0
    else:
        match_score = round(
            (len(matched_skills) / len(job_skills)) * 100
        )

    # Generate recommendation
    if match_score >= 80:
        recommendation = (
            "Excellent match. Your resume aligns well with the job requirements."
        )
    elif match_score >= 60:
        recommendation = (
            "Good match. Consider improving the missing skills before applying."
        )
    elif match_score >= 40:
        recommendation = (
            "Moderate match. Your resume needs improvement in several required skills."
        )
    else:
        recommendation = (
            "Low match. Focus on the missing skills required for this role."
        )

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendation": recommendation
    }