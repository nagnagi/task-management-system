import subprocess
from pathlib import Path

class Latex:
    def __init__(self):
        self.parent = str(Path(__file__).parent)
        self.outdir = self.parent + '/out/'
        self.file = self.parent + '/main.tex'

    def compile(self):
        cmd = 'lualatex --output-directory=' + self.outdir + ' ' + self.file
        print(cmd)
        subprocess.call(cmd)
