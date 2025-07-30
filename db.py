import sqlite3

class Databases():
    def __init__(self,name='~todo.db'):
        self.connection   = sqlite3.connection(name)
        self.cursor = self.connection.cursor ()
        
