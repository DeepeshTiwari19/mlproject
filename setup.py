from setuptools import find_packages, setup
from typing import List

HTPEN_E_DOT='-e .'

def get_requirements(file_path :str)->List[str]:
    '''
    this function return the list of requirements
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace('\n',"") for req in requirement]


#When you give "-e ." in requirements.txt file and add this and run pip install -r requirements.py if you not give this the remove this and run python setup.py install
        if HTPEN_E_DOT in requirement:
            requirement.remove(HTPEN_E_DOT)

    return requirement


# Two ways
# def get_requirements(file_path: str) -> List[str]:
#     with open(file_path, 'r') as file:
#         requirements = file.readlines()
#     return [line.strip() for line in requirements if line.strip()]





setup(
    name="Mlproject",
    version="0.0.1",
    author="Deepesh Tiwari",
    author_email="Deepesh200019@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)