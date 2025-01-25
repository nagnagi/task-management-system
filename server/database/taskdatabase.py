from database.database import DataBase
from datetime import datetime

class TaskDataBase(DataBase):
    def __init__(self):
        super().__init__()
        self.keys = ['fin', 'priority', 'add_date', 'fin_date', 'name', 'discription', 'project_id']

    def insert_task(
        self,
        priority: int,
        add_date: str,
        name: str,
        discription: str,
        project_id: int
    ):
        keys = ''
        for i in range(len(self.keys) - 1):
            keys += self.keys[i] + ', '
        keys += self.keys[len(self.keys) - 1]

        sql = 'INSERT INTO task (' + keys + ') VALUES (' \
            + '0' + ', ' \
            + str(priority) + ', '\
            + 'date("' + str(add_date) + '"), '\
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

    def get_task(self, id: int) -> str:
        return self.send_query('select * from task where id = ' + str(id) + ';')[0]

    def get_name(self, id: int) -> str:
        return self.send_query('select name from task where id = ' + str(id) + ' ;')[0][0]

    def get_id(self, name: str) -> int:
        return self.send_query('select id from task where name = "' + str(name) + '";')[0][0]

    def get_all(self) -> list[tuple]:
        return self.show_table('task')

    def delete_all(self) -> list[tuple]:
        return self.delete_from_table('task')

    def __del__(self):
        super().__del__()
