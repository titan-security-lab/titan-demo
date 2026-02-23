import sqlite3

def unsafe_login(username, password):
    """
    VULNERABLE: SQL Injection
    Attacker can inject: admin' OR '1'='1
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Direct string concatenation - VULNERABLE!
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    return cursor.fetchone()
