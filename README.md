# AI Recruitment System
Runnable Python/FastAPI recruitment system with a recruiter dashboard, using a local LLM (Ollama) and semantic search (FAISS).
Pipeline: Resume -> Parse -> Extract Details (LLM) -> Embedding -> FAISS Index -> Match with Job -> Rank Candidates -> Shortlist -> Interview -> Hire

## Features
- Upload PDF resumes and extract name, email, skills, experience and projects
- Rank candidates for a job using semantic search
- Job postings, candidate screening and shortlisting
- Hiring pipeline, interview scheduling, interview questions and feedback
- Reports with CSV export

## Run in Visual Studio / VS Code
cd AI_recruitment_sys
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
ollama pull llama3.2:3b
uvicorn main:app --reload
Open dashboard: http://127.0.0.1:8000/ui
API docs: http://127.0.0.1:8000/docs
Python 3.11+ recommended. Install [Ollama](https://ollama.com/download) and keep it running.

## Tech stack
Python, FastAPI, Ollama, Sentence Transformers, FAISS, PyMuPDF, Pydantic, HTML/CSS/JavaScript

## Note
The AI scores are estimates from resume text. A human should make the final hiring decision.
