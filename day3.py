import inputgetter
# import Set

class Santa():
    def __init__(self):
        self.x, self.y = 0, 0
        self.visited = set()
        self.visited.add((self.x, self.y))
        self.houses_delivered = 1

    def deliver_presents(self, instructions):
        for instruct in instructions:
            self._move(instruct)

        return self.houses_delivered


    def _move(self, instruction):
        if instruction == '^':
            self.y += 1
        elif instruction == '<':
            self.x -= 1
        elif instruction == 'v':
            self.y -= 1
        elif instruction == '>':
            self.x += 1

        if (self.x, self.y) not in self.visited:
            self.houses_delivered += 1
            self.visited.add((self.x, self.y))


if __name__ == '__main__':
    directions = inputgetter.get_input()
    result = Santa().deliver_presents(directions)
    print("Houses receiving at least 1 present: {}".format(result))
