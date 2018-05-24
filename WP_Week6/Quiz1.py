def sequence():
	# create a list to hold tuples which returns
	steps = []
	inWord = "MARINE"
	outWord = "AIRMEN"
	inWordList = list(inWord)
	# for every letter in MARINE
	# check if the corresponding letter is the one in AIRMEN
	# if not, switch the current index with the target index, add the tuple to the list
	for i in range (0, len(inWord)):
		if not inWordList[i] == outWord[i]:
			for j in range (i+1, len(inWord)):
				if inWordList[j] == outWord[i]:
					a, b = inWordList.index(inWordList[i]), inWordList.index(inWordList[j])
					inWordList[b], inWordList[a] = inWordList[a], inWordList[b]
					steps.append((a, b))
	# return the list 
	return steps

print(sequence())