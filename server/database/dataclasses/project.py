from dataclasses import dataclass

from database.dataclasses.data import Data

@dataclass
class Project(Data):
    id: int
    name: str
    discription: str
    due_date: str
