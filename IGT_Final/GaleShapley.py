def stableMatching(n, menPreferences, womenPreferences):
	"""
	Inputs:
		n - total n men and n women
		menPreferences - two-dimensional array of dimensions n by n, 
			contains the list of all women sorted according to their rankings by the man number i
		womenPreferences - two-dimensional array of dimensions n by n, 
			contains the list of all men sorted according to their rankings by the women number i
	Output:
		return a list of length n, where ith element is the number of woman chosen for the man number i
	"""

	assert n == len(menPreferences) and n == len(womenPreferences)

	# unmarriedMen -- the list of currently unmarried men;
	unmarriedMen = list(range(n))
	#print(unmarriedMen)
	# manSpouse -- the list of current spouses of all man;
	manSpouse = [None] * n
	#print(manSpouse)
	# womanSpouse -- the list of current spouses of all woman;
	womanSpouse = [None] * n
	# nextManChoice -- contains the number of proposals each man has made.
	nextManChoice = [0] * n

	# for each man in unmarriedMen, match him with the women using the ordering 
	while len(unmarriedMen) != 0:
		#print(unmarriedMen)
		for man in unmarriedMen:
			for woman in menPreferences[man][nextManChoice[man]:]:
				# if the woman accept the matching, (woman does not have a match or this man is a better match)
				if womanSpouse[woman] == None:
					# remove the man from unmarriedMen
					unmarriedMen.remove(man)
					# update manSpouse
					manSpouse[man] = woman
					# update womanSpouse
					womanSpouse[woman] = man
					# update nextManChoice
					nextManChoice[man] += 1
					# break, move to the next man on the list
					break
				elif betterMatch(woman, man, womenPreferences, womanSpouse):
					unmarriedMen.remove(man)
					manSpouse[man] = woman
					unmarriedMen.append(womanSpouse[woman])
					womanSpouse[woman] = man
					nextManChoice[man] += 1
					break
				# else, if the woman reject
				else:
					# update nextManChoice
					nextManChoice[man] += 1
					# match next woman
			else:
				continue
			break
	return manSpouse

def betterMatch(woman, man, womenPreferences, womanSpouse):
	"""
	Inputs:
		woman - the index of the woman in womenPreferences
		man - the index of the man in menPreferences
		womenPreferences - two-dimensional array of dimensions n by n, 
			contains the list of all men sorted according to their rankings by the women number i
		womanSpouse - the list of current spouses of all woman
	Output:
		check if the man is a better match than the current spouse for the woman
		return True if it is 
		return False if it isn't
	"""

	currentIndex = None
	manIndex = None
	# in womanSpouse, distill the current spouse for woman
	currentSpouse = womanSpouse[woman]
	# in womenPreferences[woman] (list), check the index of the current spouse for woman
	# in womenPreferences[woman] (list), check the index of the man for woman
	for i, wp in enumerate(womenPreferences[woman]):
		if wp == currentSpouse:
			currentIndex = i
		if wp == man:
			manIndex = i
	# if the index of current spouse < index of man
	if currentIndex < manIndex: return False
		# return False
	# else, return True
	return True

#print(stableMatching(1, [[0]], [[0]]))
print(stableMatching(2,  [ [0,1], [1,0] ],  [ [0,1], [1,0] ]))