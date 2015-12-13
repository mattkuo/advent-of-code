import inputgetter

VOWELS = 'aeiou'
BANNED = ['ab', 'cd', 'pq', 'xy']

def is_nice(string):
	return has_sufficient_vowels(string) and is_clean(string) and has_repeat(string)

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

if __name__ == '__main__':
	content = inputgetter.get_input().split("\n")
	count = 0
	for string in content:
		if is_nice(string):
			count += 1

	print("There are {} nice words".format(count))
