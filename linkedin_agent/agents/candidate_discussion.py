"""Agent to discuss candidate pros and cons."""

from typing import List

from .candidate_sourcing import Candidate
from .role_clarification import JobRequirement


class CandidateDiscussionAgent:
    """Evaluate candidates against job requirements."""

    def evaluate(self, requirements: JobRequirement, candidates: List[Candidate]) -> List[str]:
        summaries = []
        for c in candidates:
            pro_skills = [s for s in c.skills if s in requirements.skills]
            missing_skills = [s for s in requirements.skills if s not in c.skills]
            summary = [f"Candidate {c.name}:"]
            if pro_skills:
                summary.append(f"  Matches skills: {', '.join(pro_skills)}")
            if missing_skills:
                summary.append(f"  Missing skills: {', '.join(missing_skills)}")
            if requirements.experience_years:
                summary.append(
                    f"  Experience: {c.experience_years} years (required {requirements.experience_years})"
                )
            summaries.append("\n".join(summary))
        return summaries
