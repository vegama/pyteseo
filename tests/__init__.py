import subprocess

def tests():
    """run all available tests
    """    
    subprocess.run(["coverage", "run"])


def coverage():
    """run all available tests
    """    
    subprocess.run(["coverage", "report"])
