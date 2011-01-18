#!/usr/bin/env python
from setuptools import setup, find_packages

trove_classifiers=[
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: BSD License",
    "License :: DFSG approved",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    ]

setup(name="ostrich",
      version="0.3.4",
      description="Python port of the Scala Ostrich library",
      author="Wade Simmons",
      author_email="wade@wades.im",
      url="http://github.com/wadey/python-ostrich",
      py_modules=['ostrich'],
      packages = find_packages(),
      test_suite="ostrich.test",
      license = "Apache 2.0",
      keywords="ostrich",
      install_requires=['decorator', 'Twisted'],
      tests_require=['coverage', 'nose', 'mock'],
      classifiers=trove_classifiers,
      zip_safe = True)
