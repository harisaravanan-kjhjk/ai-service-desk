from database.ticket_repository import (
    put_tickets as repo_put_tickets,
    update_ticket as repo_update_ticket,
    get_tickets_customer as repo_get_tickets_customer,
    get_tickets as repo_get_tickets,
    assign_ticket as repo_assign_ticket,
    get_assigned_tickets as repo_get_assigned_tickets,
    get_name_by_id as repo_get_name_by_id,
    get_assigned_by_category as repo_get_assigned_by_category,
    get_title_from_id as repo_get_title_from_id,
    debug_tickets as repo_debug_tickets,
    add_note as repo_add_note
)


def put_tickets(title, description, created_by, assigned_to):
    return repo_put_tickets(
        title,
        description,
        created_by,
        assigned_to
    )


def update_ticket(ticket_id, ticket_status):
    return repo_update_ticket(
        ticket_id,
        ticket_status
    )


def get_tickets_customer(name):
    return repo_get_tickets_customer(name)


def get_tickets(ticket_id):
    return repo_get_tickets(ticket_id)


def assign_ticket(ticket_id, developer_id):
    return repo_assign_ticket(
        ticket_id,
        developer_id
    )


def get_assigned_tickets(dev_id):
    return repo_get_assigned_tickets(dev_id)


def get_name_by_id(name):
    return repo_get_name_by_id(name)


def get_assigned_by_category(dev_id, status):
    return repo_get_assigned_by_category(
        dev_id,
        status
    )


def get_title_from_id(ticket_id):
    return repo_get_title_from_id(ticket_id)


def debug_tickets():
    return repo_debug_tickets()


def add_note(ticket_id, note):
    return repo_add_note(
        ticket_id,
        note
    )
