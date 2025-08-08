import sqlite3
import os

class Databases:
    def __init__(self, name='todo.db'):
        self.db_path = os.path.expanduser(name)
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT UNIQUE,
                    completed BOOLEAN NOT NULL DEFAULT 0,
                    username TEXT NOT NULL,
                    FOREIGN KEY (username) REFERENCES users(username)
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT UNIQUE PRIMARY KEY,
                    password TEXT 
                )
            """)
            

    def get_all_posts(self,user):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM todos WHERE username = ?", (user,))
            return [row for row in cursor.fetchall()]

    def add(self, task,user):
        with self._connect() as conn:
            conn.execute("INSERT OR IGNORE INTO todos (task,username) VALUES (?,?)", (task,user,))

    def delete(self, task):
        with self._connect() as conn:
            conn.execute("DELETE FROM todos WHERE task = ?", (task,))


    def add_user(self,username,password):
        with self._connect() as conn:
            conn.execute("INSERT OR ignore INTO users (username, password) VALUES (?, ?)", (username, password))

    def get_user(self, username):
        with self._connect() as conn:
            result = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
            return result.fetchone()
    
    def get_all_usernames(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users")
            return [row[0] for row in cursor.fetchall()]

    