from database.database import DataBase
import datetime

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
            + 'date(' + str(add_date) + '), '\
            + 'null, '\
            + '"' + name + '", '\
            + '"' + discription + '", '\
            + str(project_id) + ')'
        print(sql)

        self.send_query(sql)

    def get_name(self, id: int) -> str:
        return self.send_query('select name from task where id = ' + str(id))[0][0]

    def show_all(self) -> list[tuple]:
        return self.show_table('task')

    def delete_all(self) -> list[tuple]:
        return self.delete_from_table('task')

    def __del__(self):
        super().__del__()
