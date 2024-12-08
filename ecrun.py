#!/bin/python3

from sys import argv
from easycoder import Program

if (len(argv) > 1):
    Program(argv[1:])
else:
    print('Syntax: ecrun <scriptname>')

