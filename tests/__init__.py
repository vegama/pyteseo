import subprocess

def run_all_tests():
    """run all available tests
    """    
    subprocess.run(["pytest", "-v", "--disable-warnings"])
