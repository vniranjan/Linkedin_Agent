"""Agent to source candidate data."""

import json
from dataclasses import dataclass
from typing import List
from pathlib import Path

from .role_clarification import JobRequirement


@dataclass
class Candidate:
    id: int
    name: str
    skills: List[str]
    experience_years: int
    location: str


class CandidateSourcingAgent:
    """Loads candidate profiles from data store and filters them."""

    def __init__(self, data_path: str | Path = Path(__file__).resolve().parent.parent / "data" / "candidates.json"):
        self.data_path = Path(data_path)

    def load_candidates(self) -> List[Candidate]:
        with open(self.data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Candidate(**c) for c in data]

    def search(self, requirements: JobRequirement) -> List[Candidate]:
        candidates = self.load_candidates()
        matches = []
        for candidate in candidates:
            if requirements.location and candidate.location != requirements.location:
                continue
            if requirements.experience_years and candidate.experience_years < requirements.experience_years:
                continue
            if requirements.skills and not all(skill in candidate.skills for skill in requirements.skills):
                continue
            matches.append(candidate)
        return matches
