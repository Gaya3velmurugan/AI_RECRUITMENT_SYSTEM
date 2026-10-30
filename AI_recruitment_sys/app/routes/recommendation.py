from fastapi import APIRouter
import json

from app.schemas.company import Company
from app.utils.text_formatter import company_to_text
from app.services.embedding import generate_embedding
from app.services.faiss_service import search_vector

router = APIRouter()

FILE_PATH = "app/storage/candidates.json"


@router.post("/recommend")
async def recommend(company: Company):

    company_dict = company.model_dump()

    # Convert company requirements into text
    company_text = company_to_text(company_dict)

    # Generate embedding
    embedding = generate_embedding(company_text)

    # Search similar candidates
    distances, indices = search_vector(embedding)

    # Load candidates
    with open(FILE_PATH, "r") as file:
        candidates = json.load(file)

    matched_candidates = []

    # Prevent duplicate candidates
    visited = set()

    for i, idx in enumerate(indices[0]):

        # Ignore invalid indexes
        if idx == -1:
            continue

        if idx >= len(candidates):
            continue

        # Skip duplicates
        if idx in visited:
            continue

        visited.add(idx)

        distance = float(distances[0][i])

        # Temporary match percentage
        match_percentage = max(0, min(100, round(100 - distance)))

        matched_candidates.append({
            "candidate": candidates[idx],
            "match_percentage": match_percentage,
            "distance": round(distance, 2)
        })

    # Highest match first
    matched_candidates.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return {
        "total_matches": len(matched_candidates),
        "recommended_candidates": matched_candidates
    }