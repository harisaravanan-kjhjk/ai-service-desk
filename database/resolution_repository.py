import sqlite3
from database.db import get_connection

def create_note(ticket_id,dev_id,summary,root,steps,verification):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO resolution(ticket_id,developer_id,summary,root_cause,steps_taken,verification) values(?,?,?,?,?,?)""",(ticket_id,dev_id,summary,root,steps,verification))
    id=cursor.lastrowid
    conn.commit()
    conn.close()
    return id

def update_note(ticket_id,dev_id,summary,root,steps,verification):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""update resolution set 
                   summary=?,
                   root_cause=?,
                   steps_taken=?,
                   verification=?
                   where ticket_id=? and developer_id=?""",(summary,root,steps,verification,ticket_id,dev_id))
    conn.commit()
    conn.close()

def get_resolution_by_ticket(ticket_id,dev_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from resolution where ticket_id=? and developer_id=?""",(ticket_id,dev_id))
    resolution=cursor.fetchone()
    conn.close()
    return resolution

def update_rating(ticket_id,dev_id,rating,note):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""UPDATE resolution set rating=?,note=? where developer_id=? and ticket_id=?""",(rating,note,dev_id,ticket_id))
    conn.commit()
    conn.close()
     
def get_details_for_dev_page(ticket_id,dev_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select rating,note from resolution where ticket_id=? and developer_id=?""",(ticket_id,dev_id))
    remark=cursor.fetchone()
    conn.close()
    return remark

    
#debugging function

def debug_resolution():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from resolution""")
    ret=cursor.fetchall()
    conn.close()
    return ret