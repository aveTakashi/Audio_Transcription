import os
from setuptools import setup

this_file_path = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as r:
    req = r.read().splitlines()

setup(
    name='Audio',
    version='0.3',
    author='Banabas Ave',
    description='A webapp that can transcribe audio files to text using the Watson Developer Cloud API',
    install_requires=req,
    packages=['Audio']
) 