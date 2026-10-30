def candidate_to_text(candidate: dict):
    
    # Skills
    skills = ", ".join(candidate.get("skills", []))

    # Projects
    projects = []

    for project in candidate.get("projects", []):

        if isinstance(project, dict):

            name = project.get("project_name", "")
            desc = project.get("description", "")

            projects.append(f"{name} : {desc}")

        else:

            projects.append(str(project))

    projects_text = "\n".join(projects)

    text = f"""
Candidate Name:
{candidate.get("name", "")}

Email:
{candidate.get("email", "")}

Phone:
{candidate.get("phone", "")}

Skills:
{skills}

Experience:
{candidate.get("experience", 0)} Years

Projects:
{projects_text}

Communication:
{candidate.get("communication", 0)}

Coding:
{candidate.get("coding", 0)}

Problem Solving:
{candidate.get("problem_solving", 0)}

Leadership:
{candidate.get("leadership", 0)}
"""

    return text


def company_to_text(company: dict):

    text = f"""
Company:
{company["company_name"]}

Role:
{company["role"]}

Required Skills:
{", ".join(company["required_skills"])}

Minimum Experience:
{company["minimum_experience"]} Years

Communication Score:
{company["communication_score"]}
"""

    return text