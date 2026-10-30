from pydantic import BaseModel
from typing import List


class Candidate(BaseModel):
    name: str
    skills: List[str]
    experience: int
    projects: List[str]

    communication: int
    coding: int
    problem_solving: int
    leadership: int

    email: str
    phone: str