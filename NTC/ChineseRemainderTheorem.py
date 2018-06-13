
"""
The Extend Euclid's algorithm
The function extended_gcd(a,b) returns three values: 
the greatest common divisor of a and b: d=gcd(a,b); 
and two numbers x and y such that
d = ax + by
"""
def ExtendedEuclid(a, b):
	# at least one of a and b shoud be greater than 0, and a >= b
	assert a >= b and b >= 0 and a + b > 0

	if b == 0:
		d, x, y = a, 1, 0
	else:
		(d, p, q) = ExtendedEuclid(b, a % b)
		x = q
		y = p - q * (a // b)

	assert a % d == 0 and b % d == 0
	assert d == a * x + b * y
	return (d, x, y)

"""
Chinese Remainder Theorem:
If gcd(a, b) == 1, so a and b are coprime
then, for any remainder ra mod a and any remainder rb mod b, there is an integer n:
n ≡ ra mod a 
n ≡ rb mod b

If n1 and n2 are two such integers, then
n1 ≡ n2 mod ab 

Proof:
gcd(a, b) = 1, so 1 = ax + by for some int x, y
ax ≡ 1 (mod b)
by ≡ 1 (mod a)
Thus ax corresponding to a pair of remainders (0, 1), and by corresponds to (1, 0)
Combine: (ra, rb) = ra(1, 0) + rb(0, 1)

n = raby + rbax 
	≡ raby ≡ ra (mod a)
	≡ rbax ≡ rb (mod b)
"""
def ChineseRemainderTheorem(n1, r1, n2, r2):
	"""
	Input:
		n1, n2 -  two coprime numbers
		r1 - 0 <= r1 < n1
		r2 - 0 <= r2 < n2
	Output:
		return the number r such that 0 <= r < n1n2
		r ≡ r1 mod n1 
		r ≡ r2 mod n2
	"""
	if n1 >= n2:
		d, x, y = ExtendedEuclid(n1, n2)
	else:
		d, y, x = ExtendedEuclid(n2, n1)

	#print("In function: " + str(d) + " " + str(x) + " " + str(y))

	# according to formula n = raby + rbax 
	# r = r1 * n2 * y + r2 * n1 * x
	# raby ≡ ra (mod a)
	ra = r1 * n2 * y
	# rbax ≡ rb (mod b)
	rb = r2 * n1 * x

	# mod n1n2 to get int in range (0, n1n2), r mod n1 = r mod n2 = r mod n1n2
	r = (ra + rb) % (n1 * n2)
	#print(r)

	return r

# must be between 0 and 686579304 * 26855093 = 18438151060795272
print(ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207))
#print(ExtendedEuclid(686579304, 26855093))