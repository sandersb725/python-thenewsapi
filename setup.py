try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
  
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="python-thenewsapi",
    version="0.0.1",
    author="Brighton Sanders",
    author_email="bus120610@gmail.com",
    description="A python wrapper for thenewsapi.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandersb725/python-thenewsapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
