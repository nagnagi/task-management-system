import sys
from pathlib import Path
from icecream import ic

sys.path.append(str(Path(__file__).parent.parent))

from database.taskdatabase import TaskDataBase
from database.projectdatabase import ProjectDataBase
from database.tododatabase import ToDoDataBase
from database.todolistdatabase import ToDoListDataBase

task_db = TaskDataBase()
task_db.insert_task(2, "Test Task 0", "TEST DAYO!", 1)
task_db.insert_task(1, "Test Task 1", "Motto TEST DAYO!", 1)

ic(task_db.get_all())
ic(task_db.get_name(1))

task1_id = task_db.get_id("Test Task 1")
task_db.check(task1_id)
ic(task_db[task1_id])
task_db.revert(task1_id)
ic(task_db[task1_id])

project_db = ProjectDataBase()
project_db.insert_project("Task Management System", "skdlfjawe", "2025-01-25")

ic(project_db.get_project(1))
ic(task_db.get_project(2))

todo_db = ToDoDataBase()
todo_db.insert_todo(1)
todo_db.insert_todo(2)
ic(todo_db[1])

todolist_db = ToDoListDataBase()
todolist_db.insert_todolist(1)
ic(todolist_db[1])
ic(todolist_db.get_todo(1))

task_db.delete_all()
project_db.delete_all()
todolist_db.delete_all()
