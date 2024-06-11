# from setuptools import find_packages,setup
# from typing import List

# HYPEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''this finctio will return List of requirements'''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace('\n',"") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements



# setup(
#     name='Spam Detection',
#     version='0.0.1',
#     author='Bhushan Ankush Vanjiwale',
#     author_email='rusivanjare7@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
    
# )

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return a list of requirements.'''
    requirements = []
    with open(file_path, 'r', encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Spam Detection',
    version='0.0.1',
    author='Bhushan Ankush Vanjiwale',
    author_email='rusivanjare7@gmail.com',
    description='A package for spam detection',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    # classifiers=[
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',
    #     'Operating System :: OS Independent',
    # ],
    # python_requires='>=3.6',
)
