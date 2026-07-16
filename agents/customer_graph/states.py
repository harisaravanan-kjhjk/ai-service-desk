from typing import TypedDict

class CustomerState(TypedDict):
    messages: list
    raw_response:str
    title: str
    description: str

    ticket_ready: bool
    resolution_status: str
    response: str

    level: int
    category: str
    user:str
    summary: str
    application: str
    operating_system: str
    error_code: str
    steps_tried: list[str]
    fail_attempts:int
    ticket_id:int