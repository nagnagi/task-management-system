import sys
from pathlib import Path
from icecream import ic

sys.path.append(str(Path(__file__).parent.parent))

from controller.commandline import CommandLine

while True:
    command_line = CommandLine()
    ic(command_line.input())
