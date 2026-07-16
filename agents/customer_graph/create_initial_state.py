def create_initial_state(user_id):
    return {
        "messages": [],
        "title": "",
        "description": "",
        "ticket_ready": False,
        "resolution_status": "",
        "category": "",
        "level": 1,
        "response": "",
        "summary": "",
        "application": "",
        "operating_system": "",
        "error_code": "",
        "steps_tried": [],
        "fail_attempts":0,
        "raw_response":"",
        "user":user_id
    }