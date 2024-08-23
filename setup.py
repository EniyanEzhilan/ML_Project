#This setup.py allows us to create this machine learning project as a package.. 
#So we use this whole project as a package like other packages in python for example "seaborn"
from setuptools import find_packages,setup
from typing import List

constant = "-e ."

def get_requirements(file_path:str)->List[str]:
#This function is created to return the list of requirements in the requirements.txt 
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
    #The "-e ." in requirements.txt is to connect it to the stup.py, so we dont need it here

    if constant in requirements:
        requirements.remove(constant)

    return requirements

setup(
name="ML_Project",
version="0.0.1",
author="EniyanEzhilan",
author_email="eniyanezhilan101@gmail.com",
packages=find_packages(),
install_requires= get_requirements("requirements.txt")


)