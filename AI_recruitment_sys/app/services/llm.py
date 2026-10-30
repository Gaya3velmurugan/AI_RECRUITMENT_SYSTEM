import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


def ask_llm(prompt: str):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise Exception(f"Ollama Error: {response.text}")

    return response.json()["response"]


def extract_candidate_details(resume_text: str):

    prompt = f"""
You are an AI Recruitment Assistant.

Read the resume carefully.

Extract the candidate information.

Return ONLY valid JSON.

Rules:
1. Return only JSON.
2. Do not return markdown.
3. Do not explain anything.
4. Skills must be a JSON array.
5. Projects must be a JSON array.
6. Experience must be an integer.
7. Estimate the scores based on the resume.
8. Scores must be between 0 and 100.

Return in this exact format:

{{
    "name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "experience": 0,
    "projects": [],
    "communication": 0,
    "coding": 0,
    "problem_solving": 0,
    "leadership": 0
}}

Resume:

{resume_text}
"""

    result = ask_llm(prompt)

    # Remove markdown if Ollama returns ```json ... ```
    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)