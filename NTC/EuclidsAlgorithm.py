"""
Euclid's algorithm
An efficient method for computing the greatest common divisor (GCD) of two numbers
"""
def gcd(a, b):
	assert a >= 0 and b >= 0 and a + b > 0

	while a > 0 and b > 0:
	if a >= b:
		a = a % b
	else:
		b = b % a

	return max(a, b)


print(gcd(24, 16))
print(gcd(790933790547, 1849639579327))
print(gcd(790933790548, 2))

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

extended_gcd(10,6)
extended_gcd(7,5)
extended_gcd(391,299)
extended_gcd(239,201)