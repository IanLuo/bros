from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
    name='bros',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements,
)
