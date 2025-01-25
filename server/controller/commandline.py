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
            pass
        elif words[0] == 'delete':
            pass
        elif words[0] == 'check':
            pass

    def new(self, words: list[str]):
        if words[0] == 'project':
            return self.new_project(words[1:])
        elif words[0] == 'task':
            pass
        elif words[0] == 'todo':
            pass

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
