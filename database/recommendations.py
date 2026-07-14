from database.db import get_connection

def insert_recommendations(ticket_id, developer_id, rank, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO recommendations (
            ticket_id,
            developer_id,
            rank,
            score
        )
        VALUES (?, ?, ?, ?)
    """, (ticket_id, developer_id, rank, score))

    conn.commit()
    conn.close()

def get_recommendations(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT developer_id, rank, score
        FROM recommendations
        WHERE ticket_id = ?
        ORDER BY score DESC
    """, (ticket_id,))

    recommendations = cursor.fetchall()

    conn.close()

    return recommendations

def delete_recommendations(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM recommendations
        WHERE ticket_id = ?
    """, (ticket_id,))

    conn.commit()
    conn.close()