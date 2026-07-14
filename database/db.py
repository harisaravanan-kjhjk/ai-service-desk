import sqlite3

def get_connection():
    return sqlite3.connect("app.db")

def init_db():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
create table if not exists users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE,
password TEXT,
role TEXT)""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
description text NOT NULL,
status text default "open",
createdBy integer,
assignedTo integer,
notes text)""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS recommendations (
    ticket_id INTEGER,
    developer_id INTEGER,
    rank INTEGER,
    score REAL
     )""")

#Need to change dev_name to dev_id   
    cursor.execute("""
CREATE TABLE IF NOT EXISTS resolved_logs(
                   id integer PRIMARY KEY AUTOINCREMENT,
                   dev_name text NOT NULL,
                   resolution_description NOT NULL,
                   review_rating integer default 0)
""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS resolution (
    id INTEGER PRIMARY KEY,
    ticket_id INTEGER,
    developer_id INTEGER,
    summary TEXT,
    root_cause TEXT,
    steps_taken TEXT,
    verification TEXT,
    rating integer,
    note text,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS dev_levels(
                   id integer unique,
                   dev_level integer,
                   specialization text default "versatile")""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS queue(
                   queue_id integer primary key autoincrement,
                   ticket_id integer,
                   level integer,
                   category text,
                   assigned_to integer,
                   queue_at timestamp default CURRENT_TIMESTAMP)""")
    conn.commit()
    conn.close()

