import streamlit as st
import sqlite3

def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = c.fetchone()
    conn.close()
    return data

def login():
    st.title("Login to GlowGuide")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.switch_page("camera_analysis")
        else:
            st.error("Invalid credentials. Please try again.")

    if st.button("Sign Up"):
        register_user(username, password)
        st.success("Account created! Please login.")

if __name__ == "__main__":
    create_user_table()
    login()
