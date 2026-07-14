from database.recommendations import (
    insert_recommendations as repo_insert_recommendations,
    get_recommendations as repo_get_recommendations,
    delete_recommendations as repo_delete_recommendations
)


def insert_recommendations(ticket_id, developer_id, rank, score):
    return repo_insert_recommendations(
        ticket_id,
        developer_id,
        rank,
        score
    )


def get_recommendations(ticket_id):
    return repo_get_recommendations(ticket_id)


def delete_recommendations(ticket_id):
    return repo_delete_recommendations(ticket_id)