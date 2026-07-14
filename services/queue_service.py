from database.queue_repository import (
    put_queue as repo_put_queue,
    update_queue as repo_update_queue,
    assign_ticket as repo_assign_ticket,
    get_workload as repo_get_workload,
    get_unassigned_tickets as repo_get_unassigned_tickets,
    assign_from_queue as repo_assign_from_queue,
    assign_level_category_queue as repo_assign_level_category_queue,
    get_category as repo_get_category,
    debug_queue as repo_debug_queue,
    get_level as repo_get_level
)


def put_queue(ticket_id, level):
    return repo_put_queue(
        ticket_id,
        level
    )


def update_queue(ticket_id, level):
    return repo_update_queue(
        ticket_id,
        level
    )


def assign_ticket(queue_id, dev_id):
    return repo_assign_ticket(
        queue_id,
        dev_id
    )


def get_workload(dev_id):
    return repo_get_workload(dev_id)


def get_unassigned_tickets(level):
    return repo_get_unassigned_tickets(level)


def assign_from_queue(ticket_id, developer_id):
    return repo_assign_from_queue(
        ticket_id,
        developer_id
    )


def assign_level_category_queue(queue_id, level, category):
    return repo_assign_level_category_queue(
        queue_id,
        level,
        category
    )


def get_category(ticket_id):
    return repo_get_category(ticket_id)


def debug_queue():
    return repo_debug_queue()


def get_level(ticket_id):
    return repo_get_level(ticket_id)