# LinkedIn Recruiter Agent

This project contains a simple prototype for a multi-agent recruiting assistant. It demonstrates how different agents can cooperate to clarify job requirements, search a set of sample candidates, discuss their fit, and draft outreach messages. The project is intended as a learning example and does not integrate with LinkedIn APIs or scrape data.

## Structure

- `linkedin_agent/agents/` – individual agent implementations
- `linkedin_agent/orchestrator.py` – command line interface to run the workflow
- `linkedin_agent/data/candidates.json` – sample candidate data

## Usage

Run the orchestrator from the project root:

```bash
python -m linkedin_agent.orchestrator
```

The script will prompt for job details, search the sample data, display candidate summaries and show example outreach messages.
