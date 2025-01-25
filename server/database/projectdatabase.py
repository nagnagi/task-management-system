from database.database import DataBase

from database.dataclasses.project import Project

class ProjectDataBase(DataBase):
    def __init__(self) -> None:
        super().__init__()
        self.keys = ['name', 'discription', 'due_date']

    def __del__(self) -> None:
        super().__del__()

    def __getitem__(self, index: int) -> Project:
        return self.at_to_data(index)

    def at_to_data(self, id: int) -> Project:
        return Project.from_tuple(self.at(id))

    def get_project(self, id: int) -> str:
        return self.send_query('select * from project where id = ' + str(id) + ';')[0]

    def get_name(self, id: int) -> str:
        return self.send_query('select name from project where id = ' + str(id) + ' ;')[0][0]

    def get_id(self, name: str) -> int:
        return self.send_query('select id from project where name = "' + str(name) + '";')[0][0]

    def get_all(self) -> list[tuple]:
        return self.show_table('project')
