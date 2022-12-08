# https://adventofcode.com/2022/day/2

import sys 

# Symbolic representations of values
rock = 'R'
paper = 'P' 
scissors = 'S' 

# Maps a value to its symbolic representation 
move_map = {
	'A': rock,
	'B': paper,
	'C': scissors,
	'X': rock, 
	'Y': paper, 
	'Z': scissors,
	'R': rock, 
	'P': paper, 
	'S': scissors
}

# The score this shape makes 
shape_map = {
	rock:     1,
	paper:    2,
	scissors: 3
}

# What does the input win against?
win_map = {  
	rock: scissors,
	paper: rock, 
	scissors: paper
}

# What does the input lose against? 
lose_map = { 
	rock: paper, 
	paper: scissors, 
	scissors: rock
}


'''find_score(str, str) -> int
Gives the score for this round given the opponent's and player's inputs. 
<opp>: (str) The opponent's move, in (ABCXYZRPS). 
<plr>: (str) The player's move, in (ABCXYZRPS).
returns: (int) The total score after playing the moves, from the player's 
  perspective.'''
def find_score(opp, plr): 
	opp = move_map[opp] 
	plr = move_map[plr]
	
	if   opp == plr:          contest = 3
	elif opp is rock: 
		if   plr is paper:    contest = 6
		else:                 contest = 0
	elif opp is paper: 
		if   plr is scissors: contest = 6
		else:                 contest = 0
	else: 
		if   plr is rock:     contest = 6
		else:                 contest = 0
	
	return contest + shape_map[plr]
	

'''find_move(str, str) -> (str, str)
Gives the corrected move for the player given the rule they have defined.
<opp>: (str) The opponent's move, in (ABCXYZRPS).
<plr>: (str) The player's guide move, in (XYZ).
returns: (str, str) The corrected move (opp, plr) where plr uses strategy.'''
def find_move(opp, plr): 
	opp = move_map[opp] 
	if   plr == 'X': plr = win_map[opp]
	elif plr == 'Y': plr = opp
	else:            plr = lose_map[opp]
	return opp, plr


if __name__ == '__main__': 
	if len(sys.argv) != 2: 
		print('Usage: python3 02.py <file.txt>') 
		sys.exit(1) 
	
	try: 
		data_file = open(sys.argv[1], 'r')
	except: 
		print(f'Error: file "{sys.argv[1]}" cannot be opened') 
		sys.exit(1)
	
	lines = data_file.readlines()
	data_file.close()
	
	normal = sum([
		find_score(*line.strip().split()) 
		for line in lines
	])
	strategy = sum([
		find_score(*find_move(*line.strip().split())) 
		for line in lines
	])
	
	print('Score with normal method:', normal)
	print('Score with strategy guide:', strategy) 