"""Agent to discuss candidate pros and cons."""

from typing import List

from ..llm import chat_completion

from .candidate_sourcing import Candidate
from .role_clarification import JobRequirement


class CandidateDiscussionAgent:
    """Evaluate candidates against job requirements."""

    def evaluate(
        self,
        requirements: JobRequirement,
        candidates: List[Candidate],
        *,
        use_llm: bool = False,
    ) -> List[str]:
        summaries: List[str] = []
        for c in candidates:
            if use_llm:
                prompt = (
                    "Given the following job requirements:\n"
                    f"Title: {requirements.title}\n"
                    f"Location: {requirements.location}\n"
                    f"Skills: {', '.join(requirements.skills)}\n"
                    f"Experience: {requirements.experience_years}\n\n"
                    "Summarize how well this candidate fits the role:\n"
                    f"Name: {c.name}\n"
                    f"Skills: {', '.join(c.skills)}\n"
                    f"Experience: {c.experience_years}\n"
                )
                try:
                    summary = chat_completion(prompt)
                except Exception as exc:  # noqa: PERF203
                    summary = f"LLM error: {exc}"
            else:
                pro_skills = [s for s in c.skills if s in requirements.skills]
                missing_skills = [s for s in requirements.skills if s not in c.skills]
                summary_parts = [f"Candidate {c.name}:"]
                if pro_skills:
                    summary_parts.append(f"  Matches skills: {', '.join(pro_skills)}")
                if missing_skills:
                    summary_parts.append(f"  Missing skills: {', '.join(missing_skills)}")
                if requirements.experience_years:
                    summary_parts.append(
                        f"  Experience: {c.experience_years} years (required {requirements.experience_years})"
                    )
                summary = "\n".join(summary_parts)

            summaries.append(summary)

        return summaries
