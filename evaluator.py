import re
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def words(text):
    return set(re.findall(r"\b[a-zA-Z0-9]+\b", text.lower()))

def evaluate_answer(student_answer, model_answer, keywords, max_marks):
    a = model.encode(student_answer, convert_to_tensor=True)
    b = model.encode(model_answer, convert_to_tensor=True)
    similarity = float(util.cos_sim(a, b).item())
    similarity = max(0, min(1, similarity))

    keys = [x.strip().lower() for x in (keywords or "").split(",") if x.strip()]
    if keys:
        coverage = sum(k in words(student_answer) for k in keys) / len(keys)
    else:
        coverage = similarity

    ratio = 0.70 * similarity + 0.30 * coverage
    score = round(ratio * max_marks, 2)

    if ratio >= .80:
        feedback = "Excellent answer. It is highly relevant and covers the expected concepts."
    elif ratio >= .60:
        feedback = "Good answer. Most important concepts are covered; add more detail where needed."
    elif ratio >= .40:
        feedback = "Partially correct. Add more relevant concepts and explanation."
    else:
        feedback = "Limited match with the expected answer. Review the topic and key concepts."

    return similarity, coverage, score, feedback
