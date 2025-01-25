import sqlite3
from pathlib import Path

from database.dataclasses.data import Data

class DataBase:
    def __init__(self):
        dbpath = str(Path(__file__).parent) + '/data.sqlite'
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()
        self.table_name = 'default'

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def __getitem__(self, index: int) -> Data:
        return self.at_to_data(index)

    def at_to_data(self, id: int) -> Data:
        return Data.from_tuple(self.at(id))

    def at(self, id: int) -> tuple:
        return self.send_query('select * from ' + self.table_name + ' where id = ' + str(id) + ';')[0]

    def show_table(self) -> list[tuple]:
        return self.send_query('select * from ' + self.table_name + ';')

    def delete_from_table(self) -> None:
        self.send_query('delete from ' + self.table_name + ' where 1;')

    def send_query(self, query: str) -> list[tuple]:
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.connection.commit()
        return result
