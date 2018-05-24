"""
Pay Any Large Amount with 5- and 7-Coins

Python method change(amount) that for any integer amount in the range from 24 to 1000 
returns a list consisting of numbers 5 and 7 only, 
such that their sum is equal to amount. 
For example, change(28) may return [7, 7, 7, 7], 
while change(49) may return [7, 7, 7, 7, 7, 7, 7] or [5, 5, 5, 5, 5, 5, 5, 7, 7] 
or [7, 5, 5, 5, 5, 5, 5, 5, 7].
"""

def change(amount):
	assert(amount >= 24)
	if amount == 24:
		return [5, 5, 7, 7]
	if amount == 25:
		return [5, 5, 5, 5, 5]
	if amount == 26:
		return [5, 7, 7, 7]
	if amount == 27:
		return [5, 5, 5, 5, 7]
	if amount == 28:
		return [7, 7, 7, 7]

	coins = change(amount - 5)
	coins.append(5)
	return coins


print(change(49))
