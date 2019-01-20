import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "set1problem1",
    version = "0.0.1",
    author = "",
    author_email = "",
    description = ("Family Set Problem 1. Find the relatives in the King Shan and Quen Anga's family."),
    url = "",
    packages=['Set1Problem1',],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: Freely Distributable",
    ],
    entry_points='''
        [console_scripts]
        set1problem1=set1problem1.driver:main
    ''',
    test_suite="set1problem1.tests",
)