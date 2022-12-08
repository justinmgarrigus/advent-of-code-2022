# https://adventofcode.com/2022/day/1

import sys 


''' rank_calories(list<str>) -> list<int>
Ranks each elf's calorie count and stores it within a list. 
<lines>: (list<str>) Each line of data contained within the file. Data is 
  assumed to be castable into integers. 
returns: (list<int>) A sorted list of calorie counts, where the calorie count 
  of the elf with the highest amount of calories is first.'''
def rank_calories(lines): 
	data = [0] # First elf's starting value 
	for line in lines: 
		line = line.strip() # Trailing newline 
		if len(line) > 0: 
			data[-1] += int(line)
		else:
			data.append(0) # New elf counter
	
	data.sort(reverse=True) 
	return data 


if __name__ == '__main__': 
	if len(sys.argv) != 2: 
		print('Usage: python3 01.py <file.txt>') 
		sys.exit(1) 
	
	try: 
		data_file = open(sys.argv[1], 'r')
	except: 
		print(f'Error: file "{sys.argv[1]}" cannot be opened') 
		sys.exit(1)
	
	lines = data_file.readlines()
	data_file.close() 
	
	# Ranked list of calorie counts (ranked[0] is highest) 
	ranked = rank_calories(lines)
	
	print('Highest single elf calorie:', ranked[0])
	print('Top 3 sum calories:', sum(ranked[:3]))