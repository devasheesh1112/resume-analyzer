from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Lightweight model suitable for semantic text similarity
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(
    resume_text: str,
    job_description: str
) -> float:
    """
    Calculate semantic similarity between a resume
    and a job description.

    Returns:
        Similarity score between 0 and 100.
    """

    resume_embedding = model.encode(
        [resume_text],
        normalize_embeddings=True
    )

    job_embedding = model.encode(
        [job_description],
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    score = round(float(similarity) * 100, 2)

    return max(0.0, min(score, 100.0))