import sqlite3

class DBConnect:
    def __init__(self):
        self.connection  = None

    def execute(self,query):
        self.connection = sqlite3.connect('properties/db.sqlite')
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        
    def select(self,query):
        self.connection = sqlite3.connect('properties/db.sqlite')
        cursor = self.connection.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        return record



