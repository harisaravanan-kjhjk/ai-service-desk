import json
from agents.triage_ticket import triage_ticket
from agents.l1_agent import ask_l1_agent
from .states import CustomerState
from agents.fall_back import json_repair_agent
from database.ticket_repository import put_tickets,update_ticket
from database.user_repository import *;
from agents.fall_back_triage import *
from database.queue_repository import *;
def collect_information(state):

    state["raw_response"] = ask_l1_agent(
        state["messages"],
        state
    )
    print(state)
    return state


import json

import json

def parse_information(state):

    try:
        result = json.loads(state["raw_response"])

        required_fields = [
            "title",
            "description",
            "ticket_ready",
            "resolution_status",
            "response",
            "summary",
            "application",
            "operating_system",
            "error_code",
            "steps_tried"
        ]

        missing_fields = [
            field for field in required_fields
            if field not in result
        ]

        if missing_fields:
            raise ValueError(
                f"Missing fields: {missing_fields}"
            )

        if not isinstance(result["ticket_ready"], bool):
            raise ValueError("ticket_ready must be boolean")

        if result["resolution_status"] not in [
            "resolved",
            "unresolved"
        ]:
            raise ValueError("Invalid resolution_status")

        if not isinstance(result["steps_tried"], list):
            raise ValueError("steps_tried must be a list")

        return state

    except Exception as e:
        print("Validation failed:", e)
        state["fail_attempts"] += 1
        return state


def update_status(state: CustomerState):

    try:
        result = json.loads(state["raw_response"])

        state["title"] = result["title"]
        state["description"] = result["description"]

        state["ticket_ready"] = result["ticket_ready"]
        state["resolution_status"] = result["resolution_status"]
        state["response"] = result["response"]

        state["summary"] = result.get("summary")
        state["application"] = result.get("application")
        state["operating_system"] = result.get("operating_system")
        state["error_code"] = result.get("error_code")
        state["steps_tried"] = result.get("steps_tried", [])

        state["fail_attempts"] = 0
        print(">>> update_status reached")
        return state

    except Exception as e:
        print("State update failed:", e)
        state["fail_attempts"] += 1
        return state


def failure_handler(state):

    state["raw_response"] = ""
    state["fail_attempts"] = 0

    state["response"] = (
        "I couldn't process the previous information. "
        "Please describe your issue again."
    )
    return state

def close_ticket(state):
    state["ticket_id"]=put_tickets(state["title"],state["description"],state["user"],"AI")
    update_ticket(state["ticket_id"],"resolved")
    return state

def triage_fall_back(state):
    state["raw_response"]=fall_back_triage(state["raw_response"])
    return state

def add_to_queue(state):
    print("queue/n")
    result=json.loads(state["raw_response"])
    state["category"]=result["category"]
    state["level"]=result["level"]
    queue_id=put_queue(state["ticket_id"],1)
    assign_level_category_queue(queue_id,state["level"],state["category"])
    return state

def triage_parse(state):
    try:
        print("parse_triage/n")
        result = json.loads(state["raw_response"])
        required=["category","level"]
        missing_fields=[field for field in required
                        if field not in result]
        if missing_fields:
            raise ValueError()
        return state
    except:
        state["fail_attempts"]+=1
        return state

def triage(state):
    state["ticket_id"]=put_tickets(state["title"],state["description"],state["user"],None)
    state["raw_response"] = triage_ticket(
        state["title"],
        state["description"]
    )
    print("triage/n")
    return state

def failure_handle_triage(state):
    put_queue(state["ticket_id"],1)
    return state


def fall_back(state):
    state["raw_response"]=json_repair_agent(state["raw_response"],
                                            state)
    print("fall_triage/n")
    return state