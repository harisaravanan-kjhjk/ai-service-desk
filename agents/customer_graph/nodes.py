import json
from agents.triage_ticket import triage_ticket
from agents.l1_agent import ask_l1_agent
from .states import CustomerState
from agents.fall_back import json_repair_agent
from database.ticket_repository import put_tickets,update_ticket
from database.user_repository import *;
def collect_information(state):

    state["raw_response"] = ask_l1_agent(
        state["messages"],
        state
    )

    return state


import json

def parse_information(state):

    try:
        result = json.loads(state["raw_response"])

        required_fields = [
            "title",
            "inference",
            "ticket_ready",
            "resolution_status",
            "next_question",
            "summary",
            "application",
            "operating_system",
            "error_code",
            "steps_tried"
        ]

        # Only check presence
        missing_fields = [
            field for field in required_fields
            if field not in result
        ]

        if missing_fields:
            raise ValueError(
                f"Missing fields: {missing_fields}"
            )

        return state

    except Exception as e:
        print("Validation failed:", e)

        state["fail_attempts"] += 1


        return state


def update_status(state: CustomerState):

    try:
        result = json.loads(state["raw_response"])

        state["title"] = result["title"]
        state["description"] = result["inference"]

        state["ticket_ready"] = result["ticket_ready"]
        state["resolution_status"] = result["resolution_status"]
        state["response"] = result["next_question"]

        state["summary"] = result["summary"]
        state["application"] = result["application"]
        state["operating_system"] = result["operating_system"]
        state["error_code"] = result["error_code"]
        state["steps_tried"] = result["steps_tried"]
        state["fail_attempts"]=0
        return state

    except Exception as e:
        print("State update failed:", e)
        state["fail_attempts"] += 1
        return state
    
def fall_back(state):
    state["raw_response"]


def failure_handler(state):

    state["raw_response"] = ""
    state["fail_attempts"] = 0

    state["response"] = (
        "I couldn't process the previous information. "
        "Please describe your issue again."
    )

    return state
def close_ticket(state):
    put_tickets(state["title"],state["description"],state["user"],"AI")
def triage(state):

    result = triage_ticket(
        state["title"],
        state["description"]
    )

    result = json.loads(result)

    state["category"] = result["category"]
    state["level"] = result["level"]
    
    return state

def fall_back(state):
    state["raw_response"]=json_repair_agent(state["raw_response"])
    return state