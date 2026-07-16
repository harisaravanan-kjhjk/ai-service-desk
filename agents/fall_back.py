from services.ai_service import ask_llm


def json_repair_agent(raw_response):

    prompt = f"""
You are a JSON repair agent for an IT Service Desk workflow.

Your only task is to repair the given raw response and convert it into the required JSON structure.

Rules:

1. Return ONLY valid JSON.
2. Never return markdown.
3. Never explain anything.
4. Do not solve the user's issue.
5. Do not add information that is not present.
6. Preserve available information from the raw response.
7. Fix:
   - invalid JSON syntax
   - missing quotes
   - wrong brackets
   - trailing commas
   - missing keys
   - wrong data types
8. If a value cannot be found, use null.
9. steps_tried must always be a list.
10. ticket_ready must always be boolean.
11. fail_attempts must always be 0.

Required JSON structure:

{{
    "title": null,
    "description": null,

    "ticket_ready": false,
    "resolution_status": "unresolved",
    "response": null,

    "level": null,
    "category": null,

    "summary": null,
    "application": null,
    "operating_system": null,
    "error_code": null,
    "steps_tried": [],

    "fail_attempts": 0
}}

Raw Response:

-------------------
{raw_response}
-------------------

Return only the corrected JSON.
"""

    return ask_llm(prompt)