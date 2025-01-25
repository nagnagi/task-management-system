import sqlite3
from pathlib import Path

class DataBase:
    def __init__(self):
        dbpath = str(Path(__file__).parent) + '/data.sqlite'
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def __getitem__(self, index: int) -> tuple:
        return self.at(index)

    def at(self, id: int) -> tuple:
        return self.send_query('select * from task where id = ' + str(id) + ';')[0]

    def show_table(self, table_name: str) -> list[tuple]:
        return self.send_query('select * from ' + table_name + ';')

    def delete_from_table(self, table_name: str) -> None:
        self.send_query('delete from ' + table_name + ' where 1;')

    def send_query(self, query: str) -> list[tuple]:
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.connection.commit()
        return result
