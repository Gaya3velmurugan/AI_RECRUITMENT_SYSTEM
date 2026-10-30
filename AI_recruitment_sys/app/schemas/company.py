from pydantic import BaseModel
from typing import List

class Company(BaseModel):
    company_name: str
    role: str
    required_skills: List[str]
    minimum_experience: int
    communication_score: int