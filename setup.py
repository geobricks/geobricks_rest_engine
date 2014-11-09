from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksRESTEngine',
    version='0.1.0',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Common entry point for Geobricks REST services.',
    install_requires=[
        
    ],
    url='http://pypi.python.org/pypi/GeobricksRESTEngine/'
)
