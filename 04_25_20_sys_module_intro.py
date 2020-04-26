######################################
# Intro to the sys module in python
# ---------------------------------
# sys: provides access to some of the
# modules that's used or maintained by
# the interpreter, and to functions that
# interact strongly with the interpreter.
#
#####################################

import sys

# Some of the functions in the sys module

print(sys.argv)                  # a list of command line arguments
print(sys.builtin_module_names)  # a tuple that shows all modules compiled by interpreter
print(sys.executable)            # provides the path to the python executable
# print(sys.exit(0))             # exit form python. 0 is successful termination
print(sys.getwindowsversion())  # get windows version
print(sys.hash_info)            # get the hash info
print(sys.implementation)       # get the info of your python version
print(sys.int_info)             # holds info about python's internal representation of integers
print(sys.maxsize)              # gets the max size of an integer in python
print(sys.modules)              # a dictionary that maps modules names to modules which have been loaded
print(sys.path)                 # a list of strings that specify search path for modules
print(sys.path[0])              # contains directory containing script used to invoke python interpreter
print(sys.platform)             # contains the platform identifier
print(sys.thread_info)          # a named tuple that holds info about the thread implementation
print(sys.version)              # a string that contains the version number of python
print(sys.api_version)          # the C API version for the interpreter
print(sys.version_info)         # a tuple containing 5 components of the version number


# stdin, stdout, and stderr in python
# ------------------------------------

# stdin
# -----
# used for interactive input
# including calls to input()

# read_one = sys.stdin.read()     # reads input for infinity. CTRL + C on Windows
# read_two = sys.stdin.readline()   # reads in input, could be anytype
# print(int(read_two) + 100)        # adds 100 to the user input

# stdout
# -------
# is used for the output of
# print() and expression statememts
# and for the prompts of input()

for x in sys.stdin:
    print(x, end=' ')

