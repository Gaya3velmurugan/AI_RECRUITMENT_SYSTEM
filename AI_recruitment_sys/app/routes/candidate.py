from fastapi import APIRouter, UploadFile, File
from app.schemas.candidate import Candidate

import json
import os

from app.utils.text_formatter import candidate_to_text
from app.services.embedding import generate_embedding
from app.services.faiss_service import add_vector
from app.services.resume_parser import extract_resume_text
from app.services.llm import extract_candidate_details

router = APIRouter()

FILE_PATH = "app/storage/candidates.json"
TEMP_FOLDER = "app/storage/uploads"

os.makedirs(TEMP_FOLDER, exist_ok=True)


def load_candidates():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []


def save_candidates(candidates):
    with open(FILE_PATH, "w") as file:
        json.dump(candidates, file, indent=4)


# -------------------------------------------------
# Manual Candidate Entry
# -------------------------------------------------
@router.post("/candidate")
async def add_candidate(candidate: Candidate):

    candidate_dict = candidate.model_dump()

    candidates = load_candidates()

    # Duplicate Email Check
    for existing in candidates:
        if existing.get("email", "").lower() == candidate_dict.get("email", "").lower():
            return {
                "message": "Candidate already exists.",
                "candidate": existing
            }

    candidate_text = candidate_to_text(candidate_dict)

    embedding = generate_embedding(candidate_text)

    add_vector(embedding)

    candidates.append(candidate_dict)

    save_candidates(candidates)

    return {
        "message": "Candidate Added Successfully",
        "candidate": candidate_dict
    }


# -------------------------------------------------
# Resume Upload API
# -------------------------------------------------
@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):

    file_location = os.path.join(TEMP_FOLDER, file.filename)

    with open(file_location, "wb") as f:
        f.write(await file.read())

    resume_text = extract_resume_text(file_location)

    candidate_dict = extract_candidate_details(resume_text)

    candidates = load_candidates()

    # Duplicate Email Check
    candidate_email = candidate_dict.get("email", "").lower()

    for existing in candidates:

        if existing.get("email", "").lower() == candidate_email:

            return {
                "message": "Candidate already exists.",
                "candidate": existing
            }

    candidate_text = candidate_to_text(candidate_dict)

    embedding = generate_embedding(candidate_text)

    add_vector(embedding)

    candidates.append(candidate_dict)

    save_candidates(candidates)

    return {
        "message": "Resume uploaded successfully",
        "candidate": candidate_dict
    }