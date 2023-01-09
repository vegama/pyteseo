"""Python package developed to simplify and facilitate the setup and processing of TESEO simulations (TESEO is a lagrangian numerical model developed by IHCantabria)
"""
__version__ = "0.0.1"


#  ---------------------------------------------
# NOTE - Think about move thid to cli_scripts.py
import subprocess
import pyteseo



def test():
    """run all available tests"""
    subprocess.run(["coverage", "run"])


def coverage():
    """run all available tests"""
    subprocess.run(["coverage", "report"])


def coverage_html():
    """run all available tests"""
    subprocess.run(["coverage", "report"])
    subprocess.run(["coverage", "html"])
#  ---------------------------------------------
