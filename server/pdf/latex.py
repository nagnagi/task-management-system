import subprocess
from pathlib import Path

from controller.commandline import CommandLine

from database.dataclasses.todo import ToDo
from database.dataclasses.task import Task
from database.dataclasses.project import Project

class Latex:
    def __init__(self):
        self.parent = str(Path(__file__).parent)
        self.outdir = self.parent + '/out/'
        self.file = self.parent + '/main.tex'

    def compile(self) -> str:
        cmd = 'lualatex --output-directory=' + self.outdir + ' ' + self.file
        print(cmd)
        subprocess.call(cmd)
        return cmd

    def from_id(self, id: int) -> list[str]:
        commandline = CommandLine()
        todo: list[ToDo] = commandline.exec('list todo ' + str(id))

        lines: list[str] = []
        for item in todo:
            task: Task = commandline.exec('get task ' + str(item.task_id))
            fin = '\\checkmark\\;' if task.fin else '\\Box\\;'
            priority = chr(ord('A') + task.priority)
            add_date = task.add_date
            fin_date = task.fin_date if task.fin_date else ''
            name = task.name
            project_name = commandline.exec('get project ' + str(task.project_id)).name
            lines.append(f'{fin} ({priority}) {add_date} {fin_date} {name} {project_name}')

        return lines

    def assemble(self, lines: list[str]) -> str:
        code = [
            '\\documentclass[paper=a5paper,fontsize=9pt,linegap=11pt,head_space=20mm,foot_space=20mm,gutter=15mm,fore-edge=15mm]{jlreq}',
            '\\usepackage{luatexja-fontspec}',
            '\\usepackage{amssymb}',
            '\\setmainfont{SourceHanCodeJP-Regular}',
            '\\setmainjfont{SourceHanCodeJP-Regular}',
            '\\thispagestyle{empty}',
            '\\begin{document}'
        ]
        for line in lines:
            code.append(line + '\n')
        code.append('\\end{document}')
        for i in range(len(code)):
            code[i] += '\n'
        return ''.join(code)

    def save(self, code: str) -> str:
        with open(self.file, 'w', encoding='utf-8') as f:
            f.write(code)
        return code
