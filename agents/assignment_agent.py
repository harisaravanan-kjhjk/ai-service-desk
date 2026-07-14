from services.ai_service import ask_llm

def assign_developer(ticket, developers, history):

    prompt = f"""
    Ticket:
    {ticket}

    Developers:
    {developers}

    Previous resolutions:
    {history}

    Choose the best developer.

    Return only the developer name.
    """

    return ask_llm(prompt)