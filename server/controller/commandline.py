import sys
import os

from database.dataclasses.project import Project
from database.dataclasses.task import Task
from database.dataclasses.todo import ToDo
from database.dataclasses.todolist import ToDoList

from database.projectdatabase import ProjectDataBase
from database.taskdatabase import TaskDataBase
from database.tododatabase import ToDoDataBase
from database.todolistdatabase import ToDoListDataBase


class CommandLine:
    def __init__(self):
        self.project_db = ProjectDataBase()
        self.task_db = TaskDataBase()
        self.todo_db = ToDoDataBase()
        self.todolist_db = ToDoListDataBase()

    def input(self):
        command = input('> ')
        words = command.split()
        return self.select_method(words)

    def select_method(self, words: list[str]):
        if words[0] == 'new':
            return self.new(words[1:])
        elif words[0] == 'get':
            return self.get(words[1:])
        elif words[0] == 'set':
            return self.set(words[1:])
        elif words[0] == 'delete':
            pass
        elif words[0] == 'check':
            pass

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
                args.append(input(self.project_db.keys[i] + '?> '))
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
                args.append(input(self.task_db.keys[i] + '?> '))
            return self.task_db.insert_task(*args)
        elif len(words) < len(self.task_db.keys):
            raise Exception('Error') # [TODO] エラー作る
        else:
            return self.task_db.insert_task(*words)

    def new_todo(self, words: list[str]):
        return self.todolist_db.create_new_todo()

    def get(self, words: list[str]):
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
