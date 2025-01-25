import sys
import os

from controller.commandline import CommandLine

def execute_with_commandline():
    commandline = CommandLine()
    try:
        while True:
            if result := commandline.input():
                print(result)
    except KeyboardInterrupt:
        return
