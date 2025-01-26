import sys
import os
from pathlib import Path
from io import TextIOWrapper

from database.dataclasses.project import Project
from database.dataclasses.task import Task
from database.dataclasses.todo import ToDo
from database.dataclasses.todolist import ToDoList

from database.projectdatabase import ProjectDataBase
from database.taskdatabase import TaskDataBase
from database.tododatabase import ToDoDataBase
from database.todolistdatabase import ToDoListDataBase

from pdf.engine import Engine
from pdf.latex import Latex

class CommandLine:
    def __init__(
        self,
        filein: TextIOWrapper | None = None,
        fileout: TextIOWrapper | None = None,
        print_engine: Engine | None = None,
        show_prompt: bool = True
    ):
        self.project_db = ProjectDataBase()
        self.task_db = TaskDataBase()
        self.todo_db = ToDoDataBase()
        self.todolist_db = ToDoListDataBase()

        if filein is None:
            self.filein = sys.stdin
        else:
            self.filein = filein
        if fileout is None:
            self.fileout = sys.stdout
        else:
            self.fileout = fileout

        if print_engine is None:
            self.engine = Latex()
        else:
            self.engine = print_engine

        self.show_prompt = show_prompt

    def read_line(self, prompt: str) -> str:
        if self.show_prompt:
            self.fileout.write(prompt)
            self.fileout.flush()
        return self.filein.readline().strip('\n')

    def input(self):
        command = self.read_line('> ')
        words = command.split()
        return self.select_method(words)

    def exec(self, command: str):
        words = command.split()
        return self.select_method(words)

    def select_method(self, words: list[str]):
        if words[0] == 'new':
            return self.new(words[1:])
        elif words[0] == 'get':
            return self.get(words[1:])
        elif words[0] == 'list':
            return self.list_(words[1:])
        elif words[0] == 'set':
            return self.set(words[1:])
        elif words[0] == 'delete':
            return self.delete(words[1:])
        elif words[0] == 'check':
            return self.check(words[1:])
        elif words[0] == 'revert':
            return self.revert(words[1:])
        elif words[0] == 'help':
            return self.help()

    def new(self, words: list[str]):
        if words[0] == 'project':
            return self.new_project(words[1:])
        elif words[0] == 'task':
            return self.new_task(words[1:])
        elif words[0] == 'todo':
            return self.new_todo(words[1:])

    def new_project(self, words: list[str]):
        if len(words) == 0:
            args = []
            for i in range(len(self.project_db.keys)):
                args.append(self.read_line(self.project_db.keys[i] + '?> '))
            return self.project_db.insert_project(*args)
        elif len(words) < len(self.project_db.keys):
            raise Exception('Error') # [TODO] エラー作る
        else:
            return self.project_db.insert_project(*words)

    def new_task(self, words: list[str]):
        if len(words) == 0:
            args = []
            for i in range(len(self.task_db.keys)):
                if self.task_db.keys[i] == 'fin':
                    continue
                if self.task_db.keys[i] == 'add_date':
                    continue
                if self.task_db.keys[i] == 'fin_date':
                    continue
                args.append(self.read_line(self.task_db.keys[i] + '?> '))
            return self.task_db.insert_task(*args)
        elif len(words) < len(self.task_db.keys) - 3:
            raise Exception('Error') # [TODO] エラー作る
        else:
            return self.task_db.insert_task(*words)

    def new_todo(self, words: list[str]):
        return self.todolist_db.create_new_todo()

    def get(self, words: list[str]):
        if words[0] == 'project':
            return self.project_db[int(words[1])]
        elif words[0] == 'task':
            return self.task_db[int(words[1])]
        elif words[0] == 'todolist':
            return self.todolist_db[int(words[1])]
        elif words[0] == 'todo':
            self.todo_db = ToDoDataBase(int(words[1]))
            return self.todo_db[int(words[2])]

    def list_(self, words: list[str]):
        if words[0] == 'project':
            return list(map(Project.from_tuple, self.project_db.get_all()))
        elif words[0] == 'task':
            return list(map(Task.from_tuple, self.task_db.get_all()))
        elif words[0] == 'todolist':
            return list(map(ToDoList.from_tuple, self.todolist_db.get_all()))
        elif words[0] == 'todo':
            self.todo_db = ToDoDataBase(int(words[1]))
            return list(map(ToDo.from_tuple, self.todo_db.get_all()))

    def set(self, words: list[str]):
        if words[0] == 'todo':
            return self.set_todo(words[1:])

    def set_todo(self, words: list[str]):
        self.todo_db = ToDoDataBase(int(words[0]))
        return self.todo_db.insert_todo(int(words[1]))

    def delete(self, words: list[str]):
        if words[0] == 'project':
            return self.project_db.delete_at(int(words[1]))
        elif words[0] == 'task':
            return self.task_db.delete_at(int(words[1]))
        elif words[0] == 'todolist':
            return self.todolist_db.delete_at(int(words[1]))
        elif words[0] == 'todo':
            self.todo_db = ToDoDataBase(words[1])
            return self.todo_db.delete_at(int(words[2]))

    def check(self, words: list[str]):
        if words[0] == 'task':
            return self.check_task(words[1:])

    def check_task(self, words: list[str]):
        return self.task_db.check(int(words[0]))

    def revert(self, words: list[str]):
        if words[0] == 'task':
            return self.revert_task(words[1:])

    def revert_task(self, words: list[str]):
        return self.task_db.revert(int(words[0]))

    def help(self):
        with open(str(Path(__file__).parent) + '/help.txt', 'r', encoding='utf-8') as f:
            return f.read()
