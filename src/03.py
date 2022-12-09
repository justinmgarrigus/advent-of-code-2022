# https://adventofcode.com/2022/day/3

import sys 


'''find_duplicate(str) -> str
Finds the item that appears in both compartments in the given rucksack. 
<line>: (str) The rucksack as it appears in the file. Split into two halves; the
  length of the line must therefore be divisible by two.  
returns: (str) The single item type (len = 1) that appears in both 
  compartments.''' 
def find_duplicate(line): 
	sep = len(line) // 2 
	parts = line[0:sep], line[sep:]
	return {c for c in parts[0] if c in parts[1]}.pop() # only one item
	

'''find_badge(list<str>) -> str
Finds the item that appears in each of the three parts of the group. 
<group>: (list<str>) The group of 3 elves, with a single item (str) shared
  between them.
returns: (str) The single item type (len = 1) that appears in each part.'''
def find_badge(group): 
	return {c for c in group[0] if c in group[1] and c in group[2]}.pop() 
	

'''priority(item_ch) -> int 
Finds the priority of an item. 
<item_ch>: (str) The item represented as an alphabetic character, either 
  uppercase or lowercase.
returns: (int) The priority of the item.'''  
def priority(item_ch):
	if item_ch >= 'a':
		return ord(item_ch) - ord('a') + 1
	else:
		return ord(item_ch) - ord('A') + 27


if __name__ == '__main__': 
	if len(sys.argv) != 2: 
		print('Usage: python3 03.py <file.txt>') 
		sys.exit(1) 
	
	try: 
		data_file = open(sys.argv[1], 'r')
	except: 
		print(f'Error: file "{sys.argv[1]}" cannot be opened') 
		sys.exit(1)
	
	lines = [line.strip() for line in data_file.readlines()]
	data_file.close()
	
	priority_sum = sum(priority(find_duplicate(line)) for line in lines)
	print('Priority sum:', priority_sum)
	
	# Every 3 lines are a group 
	groups = [lines[i*3 : i*3+3] for i in range(len(lines) // 3)]
	badge_sum = sum(priority(find_badge(group)) for group in groups) 
	print('Badge sum:', badge_sum) 