#!/bin/python3

from sys import argv
from easycoder import Program

if (len(argv) > 1):
    Program(argv)
else:
    print('Syntax: ./ecrun.py <scriptname> [plugins]')

# Example 1: ./ecrun.py benchmark.ecs

# The system also allows extra modules to be loaded dynamically at runtime, that add functionality to the language:

# Example 2: ./ecrun.py controller.ecs engines:Engine1

# where the added module is in a file called 'engines.py' and
# contains a class called 'Engine1'. Please consult the documentation
# on creating plugins.
