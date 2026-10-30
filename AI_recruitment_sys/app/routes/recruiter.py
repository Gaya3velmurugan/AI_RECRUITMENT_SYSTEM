from fastapi import APIRouter
from pydantic import BaseModel
import json

from app.services.llm import ask_llm

router = APIRouter()


class RecruiterPrompt(BaseModel):
    prompt: str


@router.post("/recruiter_prompt")
async def recruiter_prompt(data: RecruiterPrompt):

    prompt = f"""
You are an AI Recruitment Assistant.

Convert the following recruiter requirement into JSON.

Return ONLY JSON.

Required format:

{{
"company_name":"",
"role":"",
"required_skills":[],
"minimum_experience":0,
"communication_score":0
}}

Recruiter Requirement:

{data.prompt}
"""

    response = ask_llm(prompt)

    try:
        structured = json.loads(response)
    except:
        return {
            "error": "LLM returned invalid JSON",
            "response": response
        }

    return structured