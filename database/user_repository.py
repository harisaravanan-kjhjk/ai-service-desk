import sqlite3
from database.db import get_connection

def store_user(name,password,role):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
INSERT INTO USERS(name,password,role) VALUES(?,?,?)
                   """,(name,password,role))
    conn.commit()
    conn.close()

def get_user(name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from users where name=?""",(name,))
    user=cursor.fetchone()
    conn.close()
    return user

def get_developer():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT * FROM users WHERE role=?""",
    ("developer",))
    dev_list=cursor.fetchall()
    conn.close()
    return dev_list

def get_occupied_developers(level):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select t.assignedTo from tickets t join dev_levels u on t.assignedTo==u.dev_name  where u.dev_level=?""",(level,))
    names=cursor.fetchall()
    conn.close()
    return names

# reedundant feature must refactor
def get_by_id(id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select name from users where id=?""",(id,))
    name=cursor.fetchone()
    conn.close()
    return name

def get_by_name(name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select id from users where name=?""",(name,))
    id=cursor.fetchone()
    conn.close()
    return id