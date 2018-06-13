"""
function squares(n, m) that 
returns the minimum number of same size squares 
required to tile a grid of size n * m
"""

def gcd(a, b):
	assert a >= 0 and b >= 0 and a + b > 0

	while a > 0 and b > 0:
		if a >= b:
			a = a % b
		else:
			b = b % a

	return max(a, b)

def squares(n, m):
	# find the gcd of m and n, which is maximum size square to tile the rec, d * d
	# return n / d + m / d
	assert n > 0 and m > 0

	d = gcd(n, m)
	return n / d * m / d

print(squares(1, 1))