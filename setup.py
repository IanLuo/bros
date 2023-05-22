from setuptools import setup, find_packages

setup(
    name='bros',
    version='1.0',
    install_requires=open('requirements.txt').readlines(),
)
