import datetime
import sqlite3, jwt
from config import secret

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(256), password VARCHAR(256))")
    c.execute("INSERT INTO users(username, password) VALUES('admin', ?)", (secret, ))
    conn.commit()
    conn.close()

def get_database_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def user_registered(username, password):
    conn = get_database_connection()
    valid = conn.execute("SELECT * FROM users WHERE username=? and password=?", (username, password)).fetchall()

    if len(valid) > 0 :
        return create_token(username) 

    return None
    conn.commit()
    conn.close()
    
def create_token(username):
    payload = {
        "id":"1",
        "username":username,
        "is_admin":True,
        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=90)
    }

    token = jwt.encode(payload, secret, algorithm='HS256')

    return token

def verify_token(token):
    try:
        decoded = jwt.decode(token, secret, algorithms='HS256')
        return decoded
    except jwt.InvalidTokenError:
        return None
