import inputgetter
import functools

def solve(content):
    step = lambda acc, curr: acc + (1 if curr == '(' else -1)
    return functools.reduce(step, content, 0)

def solve2(content):
    floor = 0
    for i, instruction in enumerate(content):
        floor += (1 if instruction == '(' else -1)
        if floor == -1:
            return i + 1

if __name__ == '__main__':
    content = inputgetter.get_input()
    print("Floor #: {}".format(solve(content)))
    print("First reached basement at instruction #: {}".format(solve2(content)))
