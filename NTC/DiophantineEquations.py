"""
Diophantine Equations

Given three numbers a>0, b>0, and c, the algorithm should return some x and y such that

a x + b y = c 
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

def diophantine(a, b, c):
	assert c % gcd(a, b) == 0
	# return (x, y) such that a * x + b * y = c
	if a >= b:
		d, x, y = extended_gcd(a, b)
	else:
		d, y, x = extended_gcd(b, a)
	t = c / d # c = td
	# c = ax + by = d (px + qy); t = px + qy
	x = x * t
	y = y * t
	return (x, y)

#print(extended_gcd(5, 3))
print(diophantine(3, 5, 22))