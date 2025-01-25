import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from database.taskdatabase import TaskDataBase

task_db = TaskDataBase()
task_db.insert_task(2, '2025-01-25', "Test Task", "TEST DAYO!", 1)
print(task_db.get_name(1))
task_db.delete_all()
