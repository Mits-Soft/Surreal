# setup.py
from setuptools import setup, find_packages

setup(
    name="Surreal",
    version="0.1.0",
    author="Marco Antonio Calviño Coira",
    author_email="mits.soft.main@gmail.com",
    description="A console to access an api",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mits-Soft/Surreal",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[],
)