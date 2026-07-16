from langgraph.graph import StateGraph

from .states import CustomerState
from .nodes import *
from .edges import *

builder = StateGraph(CustomerState)

builder.add_node(
    "collect_information",
    collect_information
)

builder.add_node(
    "triage",
    triage
)

builder.add_node(
    "update_state",
    update_status
)

builder.add_node(
    "parse_information",
    parse_information
)

builder.add_node(
    "fall_back",
    fall_back
)

builder.add_node(
    "close_ticket",
    close_ticket
)

builder.add_node(
    "failure_handler",
    failure_handler
)

builder.set_entry_point(
    "collect_information"
)

builder.add_edge(
    "collect_information",
    "parse_information"
)

builder.add_conditional_edges(
    "parse_information",
    check_parse_status,
    {
        "success":"update_status",
        "repair":"fall_back",
        "failure":"failure_handler"
    }
)

builder.add_edge(
    "fall_back",
    "parse_information"
)

builder.add_edge(
    "failure_handler",
    "__end__"
)

builder.add_edge(
    "close_ticket",
    "__end__"
)

builder.add_conditional_edges(
    "update_status",
    ticket_ready
)

builder.add_edge(
    "triage",
    "__end__"
)

graph = builder.compile()