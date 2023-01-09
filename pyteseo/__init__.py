"""Python library to centralize and standarize python modules to manage TESEO model
"""
__version__ = "0.0.1"


#  ---------------------------------------------
# NOTE - Think about move thid to cli_scripts.py
import subprocess
from pathlib import Path



def test():
    """run all available tests"""
    subprocess.run(["python", "-m", "coverage", "run", Path(__file__).parent])


def coverage():
    """run all available tests"""
    subprocess.run(["coverage", "report"])


def coverage_html():
    """run all available tests"""
    subprocess.run(["coverage", "report"])
    subprocess.run(["coverage", "html"])
#  ---------------------------------------------
