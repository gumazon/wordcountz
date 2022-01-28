# read version from installed package
from importlib.metadata import version

__version__ = version("wordcountz")

from .wordcountz import count
