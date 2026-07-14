from services.ai_service import ask_llm

def evaluate_resolution(ticket, summary, root_cause, steps_taken, verification):

    prompt = f"""
You are a senior software engineer reviewing a ticket resolution.

Ticket:
{ticket}

Resolution Summary:
{summary}

Root Cause:
{root_cause}

Steps Taken:
{steps_taken}

Verification:
{verification}

Evaluate the quality of the resolution.

Consider:
- Whether the resolution addresses the ticket.
- Whether the root cause is clearly identified.
- Whether the steps taken are complete and logical.
- Whether the verification proves the issue was resolved.
- Whether the documentation is professional and sufficiently detailed.

Return ONLY valid JSON.

Schema:

{{
    "rating": <integer from 0 to 100>,
    "suggestion": "<single actionable improvement suggestion>"
}}
"""
    return ask_llm(prompt)