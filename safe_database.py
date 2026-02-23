import sqlite3

def safe_login(username, password):
    """
    SAFE: Using parameterized queries
    Prevents SQL injection
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Parameterized query - SAFE!
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    
    return cursor.fetchone()

def safe_insert(user_data):
    """
    SAFE: Proper input validation and parameterization
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Validate inputs
    if not isinstance(user_data.get('age'), int):
        raise ValueError("Age must be integer")
    
    # Parameterized insert
    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        (user_data['name'], user_data['age'])
    )
    conn.commit()
