# Introduction
This is the Python version of EasyCoder, a high-level English-like scripting language suited for prototyping and rapid testing of ideas. It operates on the command line.

The JavaScript version of EasyCoder, which provides a full set of graphical features to run in a browser, is at [https://easycoder.github.io](https://easycoder.github.io)

## Quick Start
1: Install EasyCoder in your Python environment:
```
pip install easycoder@git+https://github.com/easycoder/easycoder.git
```
2: Write a test script, 'test.ecs':
```
!   print `Hello, world!`
```
This is traditionally the first program to be written in virtually any language. To run it, launch Python and type the following commands:
```
from easycoder import Program
Program(['test.ecs'])
```
The output will look like this:
```
Compiled <anon>: 1 lines (2 tokens) in 0 ms
Run <anon>
1-> Hello, world!
```
To avoid having to use REPL you can set up a simple command such as this `bash` script, calling it `test.py`:
```
#!/bin/python3

from easycoder import Program
Program(['test.ecs'])
```
The script is passed in as a list because it could be just one of a number of command-line arguments.

When given execute permission this runs with the simple command `./test.py`. In the repository is a simple `ecrun.py` script that if placed in your working directory and given execute permission will run any EasyCoder file.

It's conventional to add a program title:
```
!   Test script

    script Test

    print `Hello, world!`
```
The first line here is just a comment and has no effect on the running of the script. The second line gives the script a name, which is useful in debugging as it says which script was running. The output is now
```
Compiled Test: 5 lines (4 tokens) in 0 ms
Run Test
5-> Hello, world!
```
