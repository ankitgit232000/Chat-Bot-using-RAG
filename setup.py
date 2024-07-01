from setuptools import find_packages , setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    """this function will return the list of requirement"""
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

setup(
    name=Chat-Bot-using-RAG,
    version="0.0.1",
    author="Ankit",
    author_email="ankitdude2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)