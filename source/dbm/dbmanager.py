# source/dbm/dbmanager.py

import sqlite3
from . import DB_PATH


class DBManager:
    """
    Module that communicates between fitness app and database which stores the data
    """

    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('CREATE TABLE Players (Player_ID INTEGER PRIMARY KEY)')
        self.cursor.execute("ALTER TABLE Players ADD COLUMN 'P_Name' TEXT")
        self.cursor.execute('INSERT OR IGNORE INTO Players (P_Name) VALUES ("Sergio Ramos")')
        self.connection.commit()

    def query(self):
        pass

    def close(self):
        self.connection.commit()
        self.connection.close()
