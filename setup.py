try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='python-thenewsapi',
	packages=['thenewsapi'],
	version='0.0.1',
	description='A python wrapper for thenewsapi.com',
	author='Brighton Sanders',
	url='https://github.com/sandersb725/python-thenewsapi',
	long_description=long_description,
	long_description_content_type="text/markdown",
	author_email='bus120610@gmail.com',
	classifiers = [
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3'
	],
)
