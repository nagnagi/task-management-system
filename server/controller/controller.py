import sys
import os

from controller.printablecmd import PrintableCommandLine

def execute_with_commandline():
    commandline = PrintableCommandLine()
    try:
        while True:
            if result := commandline.input():
                print(result)
    except KeyboardInterrupt:
        return
