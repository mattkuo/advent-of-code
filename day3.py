import inputgetter

class Santa():
    def __init__(self):
        self.x, self.y = 0, 0
        self.rx, self.ry = 0, 0
        self.visited = set()
        self.visited.add((self.x, self.y))
        self.houses_delivered = 1

    def deliver_presents(self, instructions):
        for instruct in instructions:
            self.x, self.y = self._move(instruct, self.x, self.y)

        return self.houses_delivered

    def deliver_presents_with_robot(self, instructions):
        for i, instruct in enumerate(instructions):
            if i % 2 == 0:
                self.x, self.y = self._move(instruct, self.x, self.y)
            else:
                self.rx, self.ry = self._move(instruct, self.rx, self.ry)

        return self.houses_delivered

    def _move(self, instruction, x, y):
        if instruction == '^':
            y += 1
        elif instruction == '<':
            x -= 1
        elif instruction == 'v':
            y -= 1
        elif instruction == '>':
            x += 1

        if (x, y) not in self.visited:
            self.houses_delivered += 1
            self.visited.add((x, y))

        return x, y

if __name__ == '__main__':
    directions = inputgetter.get_input()
    result = Santa().deliver_presents(directions)
    with_robo = Santa().deliver_presents_with_robot(directions)
    print("# Houses receiving presents: {}".format(result))
    print("# Houses receiving presents with robo: {}".format(with_robo))
