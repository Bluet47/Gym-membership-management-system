import sqlite3

DB_NAME = "GymDatabase_Generator_v2.db"

def connect():
    return sqlite3.connect(DB_NAME)

def fetch_one(query, params=()):
    with connect() as con:
        cur = con.cursor()
        cur.execute(query, params)
        return cur.fetchone()

def fetch_all(query, params=()):
    with connect() as con:
        cur = con.cursor()
        cur.execute(query, params)
        return cur.fetchall()

def execute_query(query, params=()):
    with connect() as con:
        cur = con.cursor()
        cur.execute(query, params)
        con.commit()
