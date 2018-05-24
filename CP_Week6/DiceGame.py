"""
Final Project for Combinatorics and Probability 
"""

def count_wins(dice1, dice2):
	"""
	Inputs:
		dice1 - the first dice to compare, represented as list of int
		dice2 - the second dice to compare, represented as list of int
	Output:
		The winning times as (dice1_win, dice2_win).
		A dice wins if the number on it is greater than the number on the other dice
	"""
	assert len(dice1) == 6 and len(dice2) == 6

	# 1. compute the number of times the first dice wins (out of all possible 36 choices)
	# 2. compute the number of times the second dice wins

	# create two variable to hold the winning times for both dice
	dice1_wins, dice2_wins = 0, 0
	# for each value in dice1 (v1), compare the current value to each value in dice2 (v2)
	for v1 in dice1:
	# if the v1 > v2, then increment the winning1
	# if v2 > v1, increment the winning2
		for v2 in dice2:
			if v1 > v2:
				dice1_wins += 1
			elif v1 < v2:
				dice2_wins += 1
	# return (win1, win2)
	return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
	"""
	Inputs:
		dices - the three dices to compare, represented as list of lists
	Output:
		The winning dice's index in dices.
		dice is better than another one, if it wins more frequently 
		(that is, out of all 36 possibilities, it wins in a cases, while the second one wins in b cases, and a>b)

		If there is such a dice, return its (0-based) index. Otherwise, return -1.
	"""
	assert all(len(dice) == 6 for dice in dices)

	for i in range(len(dices)):
		win_time = 0
		for k in range(len(dices)):
			if i != k:
				wins = count_wins(dices[i], dices[k])
				if wins[0] > wins[1]:
					win_time += 1
		if win_time == len(dices) - 1:
			return i

	return -1

def compute_strategy(dices):
	assert all(len(dice) == 6 for dice in dices)

	strategy = dict()
	strategy["choose_first"] = True
	strategy["first_dice"] = 0

	# check if I want to pick first
	optimal_dice = find_the_best_dice(dices)
	print(optimal_dice)
	if optimal_dice != -1:
		strategy["first_dice"] = optimal_dice

	else:
		strategy["choose_first"] = False
		strategy.pop("first_dice", None)
		for i in range(len(dices)):
			# print(i)
			for k in range(i+1, len(dices)):
				wins = count_wins(dices[i], dices[k])
				if wins[0] < wins[1]:
					strategy[i] = k
				elif wins[0] > wins[1]:
					strategy[k] = i
	return strategy

print(compute_strategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))