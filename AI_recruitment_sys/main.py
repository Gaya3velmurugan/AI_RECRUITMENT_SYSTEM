from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.routes.candidate import router as candidate_router
from app.routes.recommendation import router as recommendation_router
from app.routes.recruiter import router as recruiter_router

from app.services.faiss_service import load_index

app = FastAPI(
    title="AI Recruitment Recommendation System",
    description="GenAI Powered AI Recruitment Recommendation System using FastAPI, Ollama, FAISS and Sentence Transformers",
    version="2.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}  # hides the Schemas section in /docs
)

# Load FAISS index when server starts
load_index()

# Register Routes
app.include_router(candidate_router)
app.include_router(recruiter_router)
app.include_router(recommendation_router)


# Recruiter-facing web page
@app.get("/ui", include_in_schema=False)
def ui():
    return FileResponse("frontend/index.html")


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Recruitment Recommendation System",
        "version": "2.0",
        "ui": "Open /ui for the recruiter screen",
        "features": [
            "Resume Upload",
            "Resume Parsing",
            "LLM Candidate Extraction",
            "Recruiter Prompt Understanding",
            "Semantic Candidate Recommendation"
        ]
    }