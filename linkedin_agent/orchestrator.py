"""Simple command-line orchestrator for the recruiter agents."""

from .agents.role_clarification import RoleClarificationAgent
from .agents.candidate_sourcing import CandidateSourcingAgent
from .agents.candidate_discussion import CandidateDiscussionAgent
from .agents.outreach import OutreachAgent


def main() -> None:
    role_agent = RoleClarificationAgent()
    requirements = role_agent.clarify_requirements()

    sourcing_agent = CandidateSourcingAgent()
    candidates = sourcing_agent.search(requirements)

    if not candidates:
        print("No candidates found.")
        return

    discussion_agent = CandidateDiscussionAgent()
    summaries = discussion_agent.evaluate(requirements, candidates)
    print("Candidate summaries:")
    for summary in summaries:
        print(summary)
        print()

    outreach_agent = OutreachAgent()
    for candidate in candidates:
        msg = outreach_agent.draft_message(candidate, requirements)
        print(f"Outreach message for {candidate.name}:")
        print(msg)
        print()


if __name__ == "__main__":
    main()
