import sys
from pathlib import Path
from icecream import ic

sys.path.append(str(Path(__file__).parent.parent))

from pdf.latex import Latex

engine = Latex()

engine.compile()
