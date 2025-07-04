"""Agent to create outreach messages."""

from .candidate_sourcing import Candidate
from .role_clarification import JobRequirement
from ..llm import chat_completion


class OutreachAgent:
    """Generate basic outreach messages for approved candidates."""

    def draft_message(
        self,
        candidate: Candidate,
        requirements: JobRequirement,
        *,
        use_llm: bool = False,
    ) -> str:
        skills = ", ".join(requirements.skills)
        if use_llm:
            prompt = (
                "Write a short and friendly recruiting message.\n"
                f"Role: {requirements.title}\n"
                f"Location: {requirements.location}\n"
                f"Skills required: {skills}\n\n"
                f"Candidate name: {candidate.name}\n"
            )
            try:
                return chat_completion(prompt)
            except Exception as exc:  # noqa: PERF203
                return f"LLM error: {exc}"

        return (
            f"Hi {candidate.name},\n"
            f"We're looking for a {requirements.title} skilled in {skills} at our company.\n"
            "If you're interested, let's set up a time to chat!"
        )
