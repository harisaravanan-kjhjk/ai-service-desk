from services.ai_service import ask_llm
from vector_store.get_similar_notes import get_resolution_notes

def developer_guidance(title, description, level):

    notes = get_resolution_notes(
        title,
        description,
        level
    )

    prompt = f"""
You are assisting a software developer.

Current Ticket

Title:
{title}

Description:
{description}

Below are resolutions from similar historical tickets.

{notes}

Based on these examples:

- Identify common root causes.
- Suggest likely troubleshooting steps.
- Suggest useful verification methods.
- Mention any recurring mistakes to avoid.

Do NOT copy previous resolutions verbatim.
Do NOT assume the issue is identical.

Return JSON:

{{
    "possible_root_causes": [
        "...",
        "..."
    ],
    "recommended_steps": [
        "...",
        "..."
    ],
    "verification_methods": [
        "...",
        "..."
    ],
    "warnings": [
        "...",
        "..."
    ]
}}
"""

    return ask_llm(prompt)