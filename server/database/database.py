import sqlite3
from pathlib import Path

class DataBase:
    def __init__(self):
        dbpath = str(Path(__file__).parent) + "data.sqlite"
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
