from services.ai_service import ask_llm

def triage_ticket(title, description):

    prompt = f"""
    You are a help desk triage agent.

    Ticket Title:
    {title}

    Ticket Description:
    {description}

    Assign the ticket to exactly one category from the following list:

    - Authentication
    - Database
    - Backend
    - Frontend
    - DevOps
    - Other

    Also determine the support level:

    Level 1:
    Operational support, configuration issues,
    account access issues, guidance, no code changes.

    Level 2:
    Code changes required but no architectural changes.

    Level 3:
    Architectural changes, infrastructure changes,
    database redesign, security redesign, or major systemic changes.

    Return ONLY valid JSON:
    (example)
    {{
        "category": "Authentication",
        "level": 1
    }}
    If you cannot determine the category with confidence,
return:

{{
    "category": "Other",
    "level": 1
}}
    """

    return ask_llm(prompt)