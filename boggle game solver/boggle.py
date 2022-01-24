"""
File: boggle.py
----------------------------------------
This program would follow the rule of boggle game
to finds all the words on the grid.
After users enter 4 rows of 4 separated English letters,
the program will try to link adjacent letters to find all words.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variables
word_lst = []


def main():
	"""
	This program would follow the rule of boggle game to finds all the words on the grid.
	After users enter 4 rows of 4 separated English letters,
	the program will try to link adjacent letters to find all words.
	"""
	read_dictionary()
	boggle_lst = []
	for i in range(1, 5):
		letters = input(str(i)+' row of letters: ')
		if len(letters) != 7:
			print('Illegal input')
			break
		letters = letters.split()
		for j in range(len(letters)):
			letters[j] = letters[j].lower()
		boggle_lst.append(letters)

	if len(boggle_lst) == 4:
		find_words(boggle_lst)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word_lst
	with open(FILE, 'r') as f:
		for word in f:
			lst = word.split(' ')
			lst = word.strip()
			word_lst.append(lst)


def find_words(boggle_lst):
	"""
	:param boggle_lst: list, all letters the users enter.
	:return: all words followed the rule of boggle game.
	"""
	count_lst = [0]
	for x in range(0, 4):
		for y in range(0, 4):
			helper(boggle_lst, [(x, y)], [], count_lst, boggle_lst[x][y], x, y)

	print('There are '+str(sum(count_lst))+' words in total.')


def helper(boggle_lst, current, find_lst, count_lst, cur_s, x, y):
	# base case
	if len(current) >= 4:
		if cur_s not in find_lst and len(cur_s) >= 4:
			if cur_s in word_lst:
				print('Found "' + str(cur_s)+'"')
				count_lst[0] += 1
				find_lst.append(cur_s)
	for i in range(-1, 2):
		for j in range(-1, 2):
			if ((x+i), (y+j)) not in current:
				if 0 <= (x+i) <= 3 and 0 <= (y+j) <= 3:
					# Choose
					current.append(((x+i), (y+j)))
					cur_s += boggle_lst[x+i][y+j]
					# Explore
					if has_prefix(cur_s):
						helper(boggle_lst, current, find_lst, count_lst, cur_s, x+i, y+j)
					# Un-choose
					current.pop()
					cur_s = cur_s[:-1]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
