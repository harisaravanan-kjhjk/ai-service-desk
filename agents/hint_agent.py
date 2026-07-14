from services.ai_service import ask_llm

def generate_hints(ticket, similar_resolutions):

    prompt = f"""
    Ticket:
    {ticket}

    Previous successful resolutions:
    {similar_resolutions}

    Give debugging hints.
    """

    return ask_llm(prompt)