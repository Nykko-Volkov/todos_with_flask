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
                    task TEXT UNIQUE
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT UNIQUE PRIMARY KEY,
                    password TEXT 
                )
            """)
            

    def get_all_posts(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task FROM todos")
            return [row[0] for row in cursor.fetchall()]

    def add(self, task):
        with self._connect() as conn:
            conn.execute("INSERT OR IGNORE INTO todos (task) VALUES (?)", (task,))

    def delete(self, task):
        with self._connect() as conn:
            conn.execute("DELETE FROM todos WHERE task = ?", (task,))


    def add_user(self,username,password):
        with self._connect() as conn:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

    def get_user(self, username):
        with self._connect() as conn:
            result = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
            return result.fetchone()

    