from vector_store.vector_store import resolution_collection,ticket_collection
from database.resolution_repository import *
from database.ticket_repository import *
from database.level_repository import *
def sync_resolution(ticket_id,developer_id):

    ticket = get_tickets(ticket_id)
    resolution = get_resolution_by_ticket(ticket_id,developer_id)

    if ticket is None or resolution is None:
        return

    document = f"""

    Summary:
    {resolution[3]}

    Root Cause:
    {resolution[4]}

    Steps Taken:
    {resolution[5]}

    Verification:
    {resolution[6]}
    """

    metadata = {
        "developer_id": resolution[2],
        "rating": resolution[7] if resolution[7] else 0,
        "ticket_id": ticket_id
    }

    resolution_collection.upsert(
        ids=[f"ticket_{ticket_id}"],
        documents=[document],
        metadatas=[metadata]
    )

def sync_ticket(ticket_id):

    ticket = get_tickets(ticket_id)
    resolution = get_resolution_by_ticket(ticket_id)

    if ticket is None or resolution is None:
        return

    document = f"""

    title:
    {ticket[1]}

    description:
    {ticket[2]}
    """
    level=get_level(ticket[5])
    specialization=get_specializtion(ticket[5])
    metadata = {
        "developer_id": ticket[5],
        "ticket_id": ticket_id,
        "level":level,
        "specialization":specialization,
        "rating":resolution[7] if resolution[7] else 0
    }

    ticket_collection.upsert(
        ids=[f"ticket_{ticket_id}"],
        documents=[document],
        metadatas=[metadata]
    )