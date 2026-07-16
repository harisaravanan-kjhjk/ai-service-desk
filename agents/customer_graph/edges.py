def ticket_ready(state):

    if state["ticket_ready"] and not state["resolution"]:
        return "triage"
    elif state["ticket_ready"] and state["resolution"]:
        return "close_ticket"
    return "__end__"

def check_parse_status(state):

    if state["fail_attempts"] == 0:
        return "success"

    if state["fail_attempts"] < 3:
        return "repair"

    return "failure"