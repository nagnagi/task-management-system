from dataclasses import dataclass

from database.dataclasses.data import Data

@dataclass
class ToDoList(Data):
    id: int
    todo_id: int
    add_date: str
