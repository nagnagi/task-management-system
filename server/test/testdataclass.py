import sys
from pathlib import Path
from icecream import ic

sys.path.append(str(Path(__file__).parent.parent))

from database.taskdatabase import TaskDataBase

from database.dataclasses.task import Task
from database.dataclasses.project import Project
from database.dataclasses.todo import ToDo

task_db = TaskDataBase()
task_db.insert_task(2, '2025-01-25', "Test Task 0", "TEST DAYO!", 1)
task_db.insert_task(1, '2025-01-25', "Test Task 1", "Motto TEST DAYO!", 1)

print(task_db[1])
print(task_db.at_to_data(2).name)
print(task_db.at(1))
print(task_db[2].to_dict())

task_db.delete_all()
