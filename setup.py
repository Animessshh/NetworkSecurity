from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_list        

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Animesh Sharma",
    author_email="animesh1205sharma@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)