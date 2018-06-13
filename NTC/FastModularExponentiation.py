import math
"""
Compute b^e mod m by log running time
"""
def FastModularExponentiation(b, e, m):
	exList = exponentialOfTwo(e)
	#print(exList)
	result = 1
	for n in exList:
		#print(2 ** n)
		#print(partialExponentiation(b, 2 ** n, m))
		result *= partialExponentiation(b, 2 ** n, m)
	while result > m:
		result -= (result // m) * m
	return result

"""
Represent any int x with the sum of 2^k + 1
"""
def exponentialOfTwo(x):
	exList = []
	while x >= 2:
		ex = int(math.log(x, 2))
		exList.append(ex)
		x -= 2 ** ex
	if x == 1:
		exList.append(0)
	return exList

"""
Compute b^e mod m by log running time with condition that e can be represented by form of 2^k
"""
def partialExponentiation(b, e, m):
	c = b
	while e > 1:
		c = (c ** 2) % m
		e = e // 2
	return c

# b = 7, e = 4, m = 11, result(c) = 3
print(FastModularExponentiation(7, 4, 11))
# b = 7, e = 13, m = 11, c = 2
print(FastModularExponentiation(7, 13, 11))
# b = 7, e = 128, m = 11, c = 9
print(FastModularExponentiation(7, 128, 11))
