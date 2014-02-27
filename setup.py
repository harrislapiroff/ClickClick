#!/usr/bin/env python

from setuptools import setup, find_packages

version = __import__('clickclick').VERSION
	
setup(
		name='clickclick',
		version='.'.join([str(v) for v in version]),
		description='Simple photo album sharing application for Django.',
		packages = find_packages(),
	)