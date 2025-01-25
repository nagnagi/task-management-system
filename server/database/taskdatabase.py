from database.database import DataBase
from datetime import datetime

from database.dataclasses.task import Task
from database.dataclasses.project import Project
from database.projectdatabase import ProjectDataBase

class TaskDataBase(DataBase):
    def __init__(self):
        super().__init__()
        self.keys = ['fin', 'priority', 'add_date', 'fin_date', 'name', 'discription', 'project_id']
        self.table_name = 'task'

    def __del__(self):
        super().__del__()

    def __getitem__(self, index: int) -> Task:
        return self.at_to_data(index)

    def at_to_data(self, id: int) -> Task:
        return Task.from_tuple(self.at(id))

    def insert_task(
        self,
        priority: int,
        name: str,
        discription: str,
        project_id: int
    ):
        keys = ''
        for i in range(len(self.keys) - 1):
            keys += self.keys[i] + ', '
        keys += self.keys[len(self.keys) - 1]

        sql = 'INSERT INTO ' + self.table_name + ' (' + keys + ') VALUES (' \
            + '0' + ', ' \
            + str(priority) + ', '\
            + 'date("' + str(datetime.now().date()) + '"), '\
            + 'null, '\
            + '"' + name + '", '\
            + '"' + discription + '", '\
            + str(project_id) + ')'
        print(sql)

        self.send_query(sql)

    def check(self, id: int) -> bool:
        fin = self.send_query('select fin from task where id = ' + str(id) + ';')[0][0]
        if not fin:
            self.send_query('update task set fin = 1 where id = ' + str(id) + ' ;')
            self.send_query(
                'update task set fin_date = date("' + str(datetime.now().date())
                + '") where id = ' + str(id) + ';'
            )
            return True
        return False

    def revert(self, id) -> bool:
        fin = self.send_query('select fin from task where id = ' + str(id) + ';')[0][0]
        if fin:
            self.send_query('update task set fin = 0 where id = ' + str(id) + ' ;')
            self.send_query(
                'update task set fin_date = null where id = ' + str(id) + ';'
            )
            return True
        return False

    def get_name(self, id: int) -> str:
        return self.send_query('select name from task where id = ' + str(id) + ' ;')[0][0]

    def get_id(self, name: str) -> int:
        return self.send_query('select id from task where name = "' + str(name) + '";')[0][0]

    def get_project(self, id: int) -> Project:
        return Project.from_tuple(ProjectDataBase().at(self[id].project_id))
