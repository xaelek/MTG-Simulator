try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Magic the Gathering Simulator',
	'author': 'xaelek'
}

setup(**config)
