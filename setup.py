# setup.py

from setuptools import setup, find_packages

setup(
    name="Llamasgard",
    version="0.0.5",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)
