from services.ai_service import ask_llm


def fall_back_triage(raw_response):

    prompt = f"""
You are a JSON repair agent.

Your ONLY task is to repair the following raw output into valid JSON.

Rules:
1. Return ONLY valid JSON.
2. Do NOT explain anything.
3. Do NOT use markdown.
4. Do NOT re-evaluate the ticket.
5. Preserve values from the raw response whenever possible.
6. If "category" is missing or invalid, use "Other".
7. If "level" is missing or invalid, use null.
8. "level" must be an integer (1, 2, or 3) or null.
9. "category" must be exactly one of:
   - Authentication
   - Database
   - Backend
   - Frontend
   - DevOps
   - Other

Required JSON schema:

{{
    "category": "Other",
    "level": null
}}

Raw Response:

------------------------
{raw_response}
------------------------

Return ONLY the corrected JSON.
"""

    return ask_llm(prompt)