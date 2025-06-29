"""Agent to interact with hiring manager and define job requirements."""

from dataclasses import dataclass, field
from typing import List

@dataclass
class JobRequirement:
    title: str
    location: str
    skills: List[str] = field(default_factory=list)
    experience_years: int | None = None


class RoleClarificationAgent:
    """Simple agent to collect job requirements from user input."""

    def clarify_requirements(self) -> JobRequirement:
        title = input("Job title: ")
        location = input("Location: ")
        skills = input("Required skills (comma separated): ")
        experience = input("Years of experience (optional): ")
        try:
            experience_years = int(experience) if experience else None
        except ValueError:
            experience_years = None

        skill_list = [s.strip() for s in skills.split(',') if s.strip()]
        return JobRequirement(title=title, location=location, skills=skill_list, experience_years=experience_years)
