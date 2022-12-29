"""Python library to centralize and standarize python modules to manage TESEO model
"""
__version__ = "0.0.1"

import subprocess


def test():
    """run all available tests"""
    subprocess.run(["coverage", "run"])


def coverage():
    """run all available tests"""
    subprocess.run(["coverage", "report"])


def coverage_html():
    """run all available tests"""
    subprocess.run(["coverage", "html"])
