"""
The number of moves required to solve the Hanoi Towers puzzle for n=1 and n=2 discs 
is equal to 1 and 3, respectively. 
Implement the recursive solution for the Hanoi Towers (described in the lectures) 
and count the number of moves for n=6 discs.
"""

def countMoves(n):
	assert(n >= 1)
	if n == 1:
		return 1
	if n == 2:
		return 3

	return 1 + countMoves(n - 1) * 2

print(countMoves(6))