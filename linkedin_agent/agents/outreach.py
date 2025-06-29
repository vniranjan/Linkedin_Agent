"""Agent to create outreach messages."""

from .candidate_sourcing import Candidate
from .role_clarification import JobRequirement


class OutreachAgent:
    """Generate basic outreach messages for approved candidates."""

    def draft_message(self, candidate: Candidate, requirements: JobRequirement) -> str:
        skills = ", ".join(requirements.skills)
        return (
            f"Hi {candidate.name},\n"
            f"We're looking for a {requirements.title} skilled in {skills} at our company.\n"
            "If you're interested, let's set up a time to chat!"
        )
