import sys

def get_input():
    if len(sys.argv) == 2:
        return open(sys.argv[1]).read()
    else:
        return input()
