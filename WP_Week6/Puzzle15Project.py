def is_permutation(p):
  return (set(p)==set(range(len(p))))
	   
print (is_permutation([0]))
print (is_permutation([0,2,1]))
print (is_permutation([1,2,3]))

def is_even_permutation(p):
	pSort = sorted(p)
	steps = []

	for i in range (0, len(p)):
		if not p[i] == pSort[i]:
			for j in range (i+1, len(p)):
				if p[j] == pSort[i]:
					a, b = i, j
					p[b], p[a] = p[a], p[b]
					steps.append((a, b))

	print(steps)
	if len(steps) % 2 == 0: return True

	return False

print (is_even_permutation([0,3,2,4,5,6,7,1,9,8]))

