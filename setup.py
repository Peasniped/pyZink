from setuptools import setup, find_packages

def parse_requirements(filename: str = "requirements.txt"):
    """
    Function to parse requirements.txt
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line and not line.startswith("#")]

setup(
    name="pyZink",
    version="0.1",
    packages=find_packages(),
    install_requires=parse_requirements(),
)
