import sys

def get_input(gen=False):
    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        if not gen:
            return f.read()
        else:
            for line in f:
                yield line
    else:
        return input()
    