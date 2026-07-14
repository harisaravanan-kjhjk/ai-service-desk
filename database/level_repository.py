from database.db import get_connection

def get_level(id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select dev_level from dev_levels where id=?""",(id,))
    lev=cursor.fetchone()
    conn.close()
    return lev

def get_specializtion(id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select specialization from dev_levels where id=?""",(id,))
    lev=cursor.fetchone()
    conn.close()
    return lev

def insert_level(id,level,specialization):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into dev_levels(id,dev_level,specialization) values(?,?,?)""",(id,level,specialization))
    conn.commit()
    conn.close()

def assigned_devs():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select id from dev_levels""")
    assigned_devs_list=cursor.fetchall()
    conn.close()
    if not assigned_devs_list:
        return None
    return assigned_devs_list

def get_dev_by_level(level):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select u.id,u.name,l.specialization from users u join dev_levels l on u.id=l.id where l.dev_level=?""",(level,))
    devs=cursor.fetchall()
    conn.close()
    return devs




#debugging function

def debug_levels():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from dev_levels""")
    ret_list=cursor.fetchall()
    conn.close()
    return ret_list