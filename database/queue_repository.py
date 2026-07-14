from database.db import get_connection

def put_queue(ticket_id,level):
     conn=get_connection()
     cursor=conn.cursor()
     cursor.execute("""insert into queue(ticket_id,level) values(?,?)""",(ticket_id,level))
     id=cursor.lastrowid
     conn.commit()
     conn.close()
     return id

def update_queue(ticket_id,level):
     conn=get_connection()
     cursor=conn.cursor()
     cursor.execute("""update queue set level=? where ticket_id=?""",(level,ticket_id))
     conn.commit()
     conn.close()

def assign_ticket(id,dev_id):
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""update queue set assigned_to=? where queue_id=?""",(dev_id,id))
      conn.commit()
      conn.close()

def get_workload(dev_id):
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""
SELECT COUNT(*)
FROM queue q
JOIN tickets t
ON q.ticket_id = t.id
WHERE q.assigned_to = ?
AND t.status = ?
""", (dev_id, "open"))
      ret=cursor.fetchone()
      conn.close()
      return ret[0]


def get_unassigned_tickets(level):
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""select ticket_id from queue where level=? and assigned_to is NULL order by queue_at ASC""",(level,))
      ids=cursor.fetchall()
      conn.close()
      return ids

def assign_from_queue(ticket_id,developer_id):
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""update queue set assigned_to=? where ticket_id=?""",(developer_id,ticket_id))
      conn.commit()
      conn.close()

def assign_level_category_queue(id,level,category):
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""update queue set level=?,category=? where queue_id=?""",(level,category,id))
      conn.commit()
      conn.close()

def get_category(ticket_id):
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""select category from queue where ticket_id=?""",(ticket_id,))
      category=cursor.fetchone()
      conn.close()
      return category[0]

#debug function

def debug_queue():
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""select * from queue""")
      ret_list=cursor.fetchall()
      conn.close()
      return ret_list

def get_level(ticket_id):
      conn=get_connection()
      cursor=conn.cursor()
      cursor.execute("""select level from queue where ticket_id=?""",(ticket_id,))
      level=cursor.fetchone()
      conn.close()
      return level[0]