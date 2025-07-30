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

    def get_all(self):
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
