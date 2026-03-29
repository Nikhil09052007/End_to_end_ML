# Craeting this to build out model as package itself.
# this code will help to connect directly with requirements.txt


from setuptools import find_packages,setup
from typing import List

# Excluding the following piece of code.
DOT_E = '-e .' # we don't want this in our list so making changes in function

def get_requirements(file_path:str)->[str]:
    # This fuction will return the list of requiremets
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if DOT_E in requirements:
            requirements.remove(DOT_E)

    return requirements


setup(
    name = 'mlproject',
    version='0.0.1',
    author = 'Nikhil',
    author_email='pandeynikhil0905@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
    

)




