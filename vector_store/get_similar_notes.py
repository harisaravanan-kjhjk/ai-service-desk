from vector_store.vector_store import ticket_collection
from database.queue_repository import get_level
from database.resolution_repository import get_resolution_by_ticket


def get_resolution_notes(title, description, level, n=20):

    query = f"""
Title:
{title}

Description:
{description}
"""

    results = ticket_collection.query(
        query_texts=[query],
        n_results=n   
    )

    metas = results["metadatas"][0]

    notes = []

    for meta in metas:

        ticket_id = meta["ticket_id"]
        dev_id=meta["developer_id"]
        if get_level(ticket_id) != level:
            continue

        resolution = get_resolution_by_ticket(ticket_id,dev_id)

        if resolution:
            notes.append({
                "developer_id":dev_id,
                "ticket_id": ticket_id,
                "summary": resolution[3],
                "root_cause": resolution[4],
                "steps_taken": resolution[5],
                "verification": resolution[6]
            })

        if len(notes) == n:
            break

    return notes