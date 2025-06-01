from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    This function reads the requirements file and returns a list of packages.
    """
    requirements=[]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject1',
    version='0.1.0',
    description='A simple machine learning project',
    author='Sandeep Sathunuri',
    author_email='sandeep.sathunuri@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)