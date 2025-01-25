import sqlite3
from datetime import datetime

from database.dataclasses.task import Task
from database.dataclasses.todo import ToDo
from database.database import DataBase
from database.taskdatabase import TaskDataBase

class ToDoDataBase(DataBase):
    def __init__(self, id: int | None = None):
        super().__init__()
        try:
            self.cursor.execute('create table todo' + str(id) + ' (id integer primary key, task_id integer);')
        except sqlite3.OperationalError:
            pass
        self.keys = ['task_id']
        self.table_name = 'todo' + str(id)

    def __del__(self):
        super().__del__()

    def __getitem__(self, index: int) -> ToDo:
        return self.at_to_data(index)

    def at_to_data(self, id: int) -> ToDo:
        return ToDo.from_tuple(self.at(id))

    def get_task(self, id: int) -> Task:
        return Task.from_tuple(TaskDataBase().at(self[id].task_id))

    def drop(self):
        return self.send_query('drop table ' + self.table_name + ';')

    def insert_todo(
        self,
        task_id: int
    ):
        keys = ''
        for i in range(len(self.keys) - 1):
            keys += self.keys[i] + ', '
        keys += self.keys[len(self.keys) - 1]

        sql = 'INSERT INTO ' + self.table_name + ' (' + keys + ') VALUES (' \
            + str(task_id) + ');'
        print(sql)

        self.send_query(sql)
