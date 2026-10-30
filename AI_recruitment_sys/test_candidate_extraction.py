from app.services.resume_parser import extract_resume_text
from app.services.llm import extract_candidate_details

text = extract_resume_text("sample_resume.pdf")

result = extract_candidate_details(text)

print(result)