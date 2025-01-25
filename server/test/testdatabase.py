import sys
from pathlib import Path
from icecream import ic

sys.path.append(str(Path(__file__).parent.parent))

from database.taskdatabase import TaskDataBase

task_db = TaskDataBase()
task_db.insert_task(2, '2025-01-25', "Test Task 0", "TEST DAYO!", 1)
task_db.insert_task(1, '2025-01-25', "Test Task 1", "Motto TEST DAYO!", 1)

ic(task_db.get_all())
ic(task_db.get_name(1))

task1_id = task_db.get_id("Test Task 1")
task_db.check(task1_id)
ic(task_db.get_task(task1_id))
task_db.revert(task1_id)
ic(task_db.get_task(task1_id))

task_db.delete_all()
