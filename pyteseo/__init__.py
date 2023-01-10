"""Python package developed to simplify and facilitate the setup and processing of TESEO simulations (TESEO is a lagrangian numerical model developed by IHCantabria)
"""
__version__ = "0.0.1"

from pathlib import Path
import pytest


def run_tests():
    """run all available tests"""
    tests_path = Path(__file__).parent
    pytest.main(["-v", "--durations=0", "--durations-min=0.05", tests_path])
