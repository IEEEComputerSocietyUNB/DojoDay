from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dojoday',
    version='0.0.1',
    description='TDD com Flask + Selenium.',
    long_description=long_description,
    author='Dayanne Fernandes e Cristiando Junior',
    author_email='dayannefernandesc@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['flask, selenium'],
)
