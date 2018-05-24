def two_three_dividsible(n):
	div_two, div_three, div_two_three = 0, 0, 0
	for i in range(1, n+1):
		if i % 2 == 0:
			div_two += 1
		if i % 3 == 0:
			div_three += 1
		if i % 2 == 0 and i % 3 == 0:
			div_two_three += 1

	return div_two + div_three - div_two_three

print(two_three_dividsible(1000))	


