def ticket_ready(state):

    if state["ticket_ready"]:

        if state["resolution_status"] == "unresolved":
            return "triage"

        else:
            return "close_ticket"

    return "__end__"

def check_parse_status(state):

    if state["fail_attempts"] == 0:
        return "success"

    if state["fail_attempts"] < 3:
        return "repair"

    return "failure"

def check_triage_parse_status(state):

    if state["fail_attempts"] == 0:
        return "success"

    if state["fail_attempts"] < 3:
        return "repair"

    return "failure"