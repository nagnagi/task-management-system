import sqlite3
from datetime import datetime

from database.dataclasses.todo import ToDo
from database.dataclasses.todolist import ToDoList
from database.database import DataBase
from database.tododatabase import ToDoDataBase

class ToDoListDataBase(DataBase):
    def __init__(self):
        super().__init__()
        self.keys = ['todo_id', 'add_date']
        self.table_name = 'todolist'

    def __del__(self):
        super().__del__()

    def __getitem__(self, index: int) -> ToDoList:
        return self.at_to_data(index)

    def at_to_data(self, id: int) -> ToDoList:
        return ToDoList.from_tuple(self.at(id))

    def get_todo(self, id: int) -> ToDo:
        return ToDo.from_tuple(ToDoDataBase().at(self[id].todo_id))

    def insert_todolist(
        self,
        todo_id: int
    ):
        keys = ''
        for i in range(len(self.keys) - 1):
            keys += self.keys[i] + ', '
        keys += self.keys[len(self.keys) - 1]

        sql = 'INSERT INTO ' + self.table_name + ' (' + keys + ') VALUES (' \
            + str(todo_id) + ', ' \
            + 'date("' + str(datetime.now().date()) + '"));'

        self.send_query(sql)
