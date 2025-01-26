import sys
from pathlib import Path
from icecream import ic

sys.path.append(str(Path(__file__).parent.parent))

from pdf.latex import Latex
from controller.commandline import CommandLine

commandline = CommandLine()

engine = Latex()

lines = engine.from_id(commandline.exec('get todolist ' + str(2)).todo_id)
print(lines)
code = engine.assemble(lines)
print(code)
engine.save(code)
engine.compile()
