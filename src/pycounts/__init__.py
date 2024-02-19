# read version from installed package
from src import *
from importlib.metadata import version
__version__ = version("pycounts")