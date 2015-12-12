import inputgetter
import functools

def solve(content):
    step = lambda acc, curr: acc + (1 if curr == '(' else -1)
    return functools.reduce(step, content, 0)

if __name__ == '__main__':
    content = inputgetter.get_input()
    print(solve(content))
