import inputgetter
import re

VOWELS = 'aeiou'
BANNED = ['ab', 'cd', 'pq', 'xy']

def is_nice(string):
	return has_sufficient_vowels(string) and is_clean(string) and has_repeat(string)

def is_nice2(string):
	return has_pairs(string) and has_burger_pairs(string)

def has_sufficient_vowels(string):
	count = 0
	for char in string:
		if char in VOWELS:
			count += 1
	return count >= 3

def is_clean(string):
	for bt in BANNED:
		if bt in string:
			return False
	return True

def has_repeat(string):
	current_char = string[0]
	for char in string[1:]:
		if char == current_char:
			return True
		else:
			current_char = char

def has_pairs(string):
	for x in range(len(string) - 1):
		if string.count(string[x:x+2], x + 2) >= 1:
			return True
	return False

def has_burger_pairs(string):
	return re.search(r"(\w)\w\1", string) is not None

if __name__ == '__main__':
	content = inputgetter.get_input().split("\n")
	count = 0
	count2 = 0
	
	for string in content:
		if is_nice(string):
			count += 1
		if is_nice2(string):
			count2 += 1

	print("There are {} nice words".format(count))
	print("There are {} nice words".format(count2))

