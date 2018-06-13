"""
Given three integers a, b, and n, such that gcd(a,n)=1 and n > 1, 
the algorithm should return an integer x such that

0 <= x <= n-1, and

b / a = x (mod n) (that is, b = ax (mod n)).
"""

def gcd(a, b):
	assert a >= 0 and b >= 0 and a + b > 0

	while a > 0 and b > 0:
		if a >= b:
			a = a % b
		else:
			b = b % a
	return max(a, b)

"""
The Extend Euclid's algorithm
The function extended_gcd(a,b) returns three values: 
the greatest common divisor of a and b: d=gcd(a,b); 
and two numbers x and y such that
d = ax + by
"""
def extended_gcd(a, b):
	# at least one of a and b shoud be greater than 0, and a >= b
	assert a >= b and b >= 0 and a + b > 0

	if b == 0:
		d, x, y = a, 1, 0
	else:
		(d, p, q) = extended_gcd(b, a % b)
		x = q
		y = p - q * (a // b)

	assert a % d == 0 and b % d == 0
	assert d == a * x + b * y
	return (d, x, y)
	
def divide(a, b, n):
	assert n > 1 and a > 0 and gcd(a, n) == 1
	
	# return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
	# 1. use the extended gcd to find s and t in nt + as = 1
	if n >= a:
		d, t, s = extended_gcd(n, a)
	else:
		d, s, t = extended_gcd(a, n)
	# 2. s is the inverse of a mod n, so b/a == b * s
	while s < 0:
		s += n
	result = b * s
	while result > n:
		result -= n
	return result

print(divide(2, 7, 9))
