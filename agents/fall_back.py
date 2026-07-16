from services.ai_service import ask_llm


def json_repair_agent(raw_response, state):

    memory_context = f"""
Current Known Information

Summary:
{state.get("summary")}

Application:
{state.get("application")}

Operating System:
{state.get("operating_system")}

Error Code:
{state.get("error_code")}

Steps Already Tried:
{state.get("steps_tried")}
"""

    prompt = f"""
You are a JSON repair agent for an IT Service Desk workflow.

Your ONLY responsibility is to repair malformed JSON.

Do NOT answer the user's question.
Do NOT troubleshoot the issue.
Do NOT invent new information.

Current Known Information:

{memory_context}

Rules:

1. Return ONLY valid JSON.
2. Never return markdown.
3. Never explain anything.
4. Repair malformed JSON syntax.
5. Preserve every piece of information already present in the raw response.
6. If information is missing from the raw response but exists in the Current Known Information, preserve the existing value.
7. Only use null when the value is unknown in both the raw response and the Current Known Information.
8. Fix:
   - missing quotes
   - missing commas
   - trailing commas
   - incorrect brackets
   - invalid JSON syntax
   - incorrect data types
9. ticket_ready must always be a boolean.
10. resolution_status must always be either "resolved" or "unresolved".
11. steps_tried must always be a JSON array.
12. Return every required field exactly once.

Required JSON structure:

{{
    "title": null,
    "description": null,

    "ticket_ready": false,
    "resolution_status": "unresolved",
    "response": null,

    "summary": null,
    "application": null,
    "operating_system": null,
    "error_code": null,
    "steps_tried": []
}}

Raw Response:

-------------------
{raw_response}
-------------------

Return ONLY the repaired JSON.
"""

    return ask_llm(prompt)