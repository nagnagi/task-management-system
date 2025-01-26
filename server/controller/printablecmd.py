from io import TextIOWrapper

from controller.commandline import CommandLine

from pdf.latex import Engine
from pdf.latex import Latex

class PrintableCommandLine(CommandLine):
    def __init__(
        self,
        filein: TextIOWrapper | None = None,
        fileout: TextIOWrapper | None = None,
        show_prompt = True,
        print_engine: Engine | None = None
    ):
        super().__init__(filein, fileout, show_prompt)
        if print_engine is None:
            self.engine = Latex()
        else:
            self.engine = print_engine

    def select_method(self, words: list[str]):
        if words[0] == 'print':
            return self.print(words[1:])
        else:
            super().select_method(words)


    def print(self, words: list[str]):
        if words[0] == 'todo':
            return self.print_todo(words[1:])

    def print_todo(self, words: list[str]):
        return self.engine.gen(int(words[0]))
