import sqlite3
from pathlib import Path

class DataBase:
    def __init__(self):
        dbpath = str(Path(__file__).parent) + '/data.sqlite'
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()

    def show_table(self, table_name: str) -> list[tuple]:
        return self.send_query('select * from ' + table_name)

    def send_query(self, query: str) -> list[tuple]:
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.connection.commit()
        return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()
