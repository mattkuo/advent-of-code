import inputgetter

def solve(content):
    result = 0
    for dimensions in content:
        los = [int(side) for side in dimensions.split('x')]
        result += _get_surface_area(los)
    return result

def _get_surface_area(los):
    l, w, h = los
    sides = l * w, w * h, h * l
    return sum(map(lambda x: 2 * x, sides)) + min(sides)


if __name__ == '__main__':
    content = inputgetter.get_input()
    print(solve(content.split("\n")))
