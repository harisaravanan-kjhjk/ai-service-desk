from database.resolution_repository import (
    create_note as repo_create_note,
    update_note as repo_update_note,
    get_resolution_by_ticket as repo_get_resolution_by_ticket,
    update_rating as repo_update_rating,
    get_details_for_dev_page as repo_get_details_for_dev_page,
    debug_resolution as repo_debug_resolution
)


def create_note(ticket_id, dev_id, summary, root, steps, verification):
    return repo_create_note(
        ticket_id,
        dev_id,
        summary,
        root,
        steps,
        verification
    )


def update_note(ticket_id, dev_id, summary, root, steps, verification):
    return repo_update_note(
        ticket_id,
        dev_id,
        summary,
        root,
        steps,
        verification
    )


def get_resolution_by_ticket(ticket_id, dev_id):
    return repo_get_resolution_by_ticket(
        ticket_id,
        dev_id
    )


def update_rating(ticket_id, dev_id, rating, note):
    return repo_update_rating(
        ticket_id,
        dev_id,
        rating,
        note
    )


def get_details_for_dev_page(ticket_id, dev_id):
    return repo_get_details_for_dev_page(
        ticket_id,
        dev_id
    )


def debug_resolution():
    return repo_debug_resolution()