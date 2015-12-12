import inputgetter

def solve(content):
    result = 0
    for dimensions in content:
        los = [int(side) for side in dimensions.split('x')]
        result += _get_wrapping_paper_area(los)
    return result

def solve2(content):
    result = 0
    for dimensions in content:
        los = [int(side) for side in dimensions.split('x')]
        result += _get_bow_length(los)
    return result

def _get_wrapping_paper_area(los):
    l, w, h = los
    sides = l * w, w * h, h * l
    return sum(map(lambda x: 2 * x, sides)) + min(sides)

def _get_bow_length(los):
    l, w, h = los
    sides = sorted([(l * w, l, w), (w * h, w, h), (h * l, h, l)])

    return 2 * (sides[0][1] + sides[0][2]) + l * w * h

if __name__ == '__main__':
    content = inputgetter.get_input().split("\n")
    print("Wrapping paper required: {}".format(solve(content)))
    print("Ribbon required: {}".format(solve2(content)))
