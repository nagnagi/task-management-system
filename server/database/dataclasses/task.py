from dataclasses import dataclass

from database.dataclasses.data import Data

@dataclass
class Task(Data):
    id: int
    fin: bool
    priority: int
    add_date: str
    fin_date: str
    name: str
    discription: str
    project_id: int
