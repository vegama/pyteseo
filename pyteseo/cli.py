from pathlib import Path
import pytest

def run_tests():
    """run all available tests"""
    tests_path = Path(__file__).parent
    print(f"Running tests from path: {tests_path}")
    pytest.main(["-v", "--durations=0", "--durations-min=0.05", tests_path])
