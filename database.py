import sqlite3

def init_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    website TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

def add_password(website, username, password):
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
              (website, username, password))
    conn.commit()
    conn.close()

def get_passwords():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    data = c.fetchall()
    conn.close()
    return data

def delete_password(password_id):
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE id=?", (password_id,))
    conn.commit()
    conn.close()
