from enum import Enum
import re
import inputgetter

class Instruction(object):
	def __init__(self, inst_type, startx, starty, endx, endy):
		self.inst_type = inst_type
		self.startx, self.starty = startx, starty
		self.endx, self.endy = endx, endy
		
	def __repr__(self):
		return "Instruction({}, {}, {}, {}, {})".format(
			self.inst_type, 
			self.startx, 
			self.starty, 
			self.endx, 
			self.endy)
	
	def perform_inst(self, grid):
		for x in range(self.startx, self.endx + 1):
			for y in range(self.starty, self.endy + 1):
				if self.inst_type == InstructionType.off:
					grid[x][y] = False
				elif self.inst_type == InstructionType.on:
					grid[x][y] = True
				else:
					grid[x][y] = not grid[x][y]

class InstructionType(Enum):
	off = 0
	on = 1
	toggle = 2

def get_next_instruction(instructions):
	inst_re = re.compile(r"^(.+) (\d+),(\d+) through (\d+),(\d+)$")
	for inst in instructions:
		match_groups = re.match(inst_re, inst)
		if not match_groups:
			raise Exception('Instruction parse error for: ' + inst)

		if match_groups.group(1) == 'turn off':
			inst_type = InstructionType.off
		elif match_groups.group(1) == 'turn on':
			inst_type = InstructionType.on
		else:
			inst_type = InstructionType.toggle
		
		yield Instruction(inst_type, 
				int(match_groups.group(2)), 
				int(match_groups.group(3)), 
				int(match_groups.group(4)), 
				int(match_groups.group(5)))
		
		
if __name__ == '__main__':
	gen = inputgetter.get_input(gen=True)
	
	grid = [[False for _ in range(1000)] for _ in range(1000)]
	
	for inst in get_next_instruction(gen):
		inst.perform_inst(grid)
		
	count = 0
	
	for row in grid:
		count += row.count(True)
		
	print("Number of lights lit: {}".format(count))