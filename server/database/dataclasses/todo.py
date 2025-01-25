from dataclasses import dataclass

from database.dataclasses.data import Data

@dataclass
class ToDo(Data):
    id: int
    task_id: int
