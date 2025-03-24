import sqlite3

def connect_db():
    conn = sqlite3.connect("glowguide.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def insert_user(username, password):
    conn = sqlite3.connect("glowguide.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
