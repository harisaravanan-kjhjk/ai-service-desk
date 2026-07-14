import json
from database.db import get_connection

def update_ticket(ticket_id,ticket_status):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""UPDATE tickets set status=? where id=?""",(ticket_status,ticket_id))
    conn.commit()
    conn.close()

def put_tickets(title,description,created_by,assignedTo):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
insert into tickets(title,description,createdBy,assignedTo) values(?,?,?,?)""",(title,description,created_by,assignedTo))
    conn.commit()
    tic=cursor.lastrowid
    conn.close()
    return tic
    
def get_tickets_customer(name):
    conn=get_connection()
    cursor=conn.cursor()
    id=get_name_by_id(name)[0]
    cursor.execute("""select * from tickets where createdBy=?""",(id,))
    ticket_list=cursor.fetchall()
    return ticket_list

def get_tickets(ticket_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from tickets where id=?""",(ticket_id,))
    ticket=cursor.fetchone()
    conn.close()
    return ticket

def assign_ticket(ticket_id,developer_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""update tickets set assignedTo=? where id=?""",(developer_id,ticket_id))
    conn.commit()
    conn.close()

def get_assigned_tickets(dev_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from tickets where assignedTo=?""",(dev_id,))
    tickets=cursor.fetchall()
    conn.close()
    return tickets

def get_name_by_id(name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select id from users where name=?""",(name,))
    id=cursor.fetchone()
    conn.close()
    return id

def get_assigned_by_category(dev_id,status):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from tickets where assignedTo=? and status=?""",(dev_id,status))
    tickets=cursor.fetchall()
    conn.close()
    return tickets

def get_title_from_id(id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select title from tickets where id=?""",(id,))
    title=cursor.fetchone()
    conn.close()
    return title


#debug tickets

def debug_tickets():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from tickets""")
    list=cursor.fetchall()
    conn.close()
    return list


def add_note(ticket_id, note):
    conn = get_connection()
    cursor = conn.cursor()

    if not isinstance(note, str):
        note = json.dumps(note, indent=2)

    cursor.execute(
        "UPDATE tickets SET notes=? WHERE id=?",
        (note, ticket_id)
    )

    conn.commit()
    conn.close()