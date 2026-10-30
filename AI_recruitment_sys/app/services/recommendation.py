print('hello')
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

    company_text = company_to_text(company_dict)

    embedding = generate_embedding(company_text)

    distances, indices = search_vector(embedding)

    with open(FILE_PATH, "r") as file:
        candidates = json.load(file)

    matched_candidates = []

    for idx in indices[0]:
        if idx < len(candidates):
            matched_candidates.append(candidates[idx])

    return {
        "recommended_candidates": matched_candidates
    }