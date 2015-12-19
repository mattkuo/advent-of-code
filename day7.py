import re
import inputgetter


class Gate(object):
    gates = {}

    def __init__(self, inst_str):
        self.inst = self._parse_instruction(inst_str)
        self.name = self.inst['dest']
        self.value = None

    def _parse_instruction(self, inst_str):
        # Match shifts LSHIFT, RSHIFT
        match = re.match(r"^(?P<src>\w+) (?P<op>LSHIFT|RSHIFT) (?P<val>\d+) -> (?P<dest>\w+)$", inst_str)
        if match:
            return match.groupdict()

        # Match AND, OR
        match = re.match(r"^(?P<src>\w+) (?P<op>AND|OR) (?P<src2>\w+) -> (?P<dest>\w+)$", inst_str)
        if match:
            return match.groupdict()

        # Match NOT
        match = re.match(r"^(?P<op>NOT) (?P<src>\w+) -> (?P<dest>\w+)$", inst_str)
        if match:
            return match.groupdict()

        # Match input value
        match = re.match(r"^(?P<src>\w+) -> (?P<dest>\w+)$", inst_str)
        dictionary = match.groupdict()
        dictionary['op'] = 'input_val'
        return dictionary

    @classmethod
    def get_val(cls, name):
        if name.isdigit():
            return int(name)

        gate = cls.gates[name]
        inst = gate.inst

        if gate.value is not None:
            return gate.value

        if inst['op'] == 'LSHIFT':
            gate.value = cls.get_val(inst['src']) << int(inst['val'])
        elif inst['op'] == 'RSHIFT':
            gate.value = cls.get_val(inst['src']) >> int(inst['val'])
        elif inst['op'] == 'AND':
            gate.value = cls.get_val(inst['src']) & cls.get_val(inst['src2'])
        elif inst['op'] == 'OR':
            gate.value = cls.get_val(inst['src']) | cls.get_val(inst['src2'])
        elif inst['op'] == 'NOT':
            gate.value = ~cls.get_val(inst['src'])
        elif inst['op'] == 'input_val':
            gate.value = cls.get_val(inst['src'])

        return gate.value

def main():
    gen = inputgetter.get_input(gen=True)

    for line in gen:
        gate = Gate(line.strip())
        Gate.gates[gate.name] = gate

    print("Value of a is: {}".format(Gate.get_val('a')))

if __name__ == '__main__':
    main()
