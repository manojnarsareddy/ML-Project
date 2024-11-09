from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT ="-e ."

def get_requirement(file_path:str)->List[str]:

    """This function will return the list of requirement"""

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 
    
    return requirements
    

setup(name="ML Project",
      version =0.01,
      author="Manoj",
      author_email="nmanoj@gmail.com",
      packages=find_packages(),
      install_requires = get_requirement("Requirement.txt")

)