from database.database import DataBase

class ProjectDataBase(DataBase):
    def __init__(self) -> None:
        super().__init__()
        self.keys = ['name', 'discription', 'due_date']

    def __del__(self) -> None:
        super().__del__()

    def get_project(self, id: int) -> str:
        return self.send_query('select * from project where id = ' + str(id) + ';')[0]

    def get_name(self, id: int) -> str:
        return self.send_query('select name from project where id = ' + str(id) + ' ;')[0][0]

    def get_id(self, name: str) -> int:
        return self.send_query('select id from project where name = "' + str(name) + '";')[0][0]

    def get_all(self) -> list[tuple]:
        return self.show_table('project')
