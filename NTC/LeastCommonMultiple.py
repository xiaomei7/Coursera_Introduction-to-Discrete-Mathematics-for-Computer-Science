"""
an efficient algorithm for finding the least common multiple of two positive integers.
"""

# idea: lcm(a, b) * gcd(a, b) = a * b

def gcd(a, b):
	assert a >= 0 and b >= 0 and a + b > 0

	while a > 0 and b > 0:
		if a >= b:
			a = a % b
		else:
			b = b % a

	return max(a, b)

def lcm(a, b):
	assert a > 0 and b > 0

	return a * b / gcd(a, b)