"""
 find a sequence of neighbor transpositions of letters that transform the sequence 
 MARINE (letters are numbered 0..5) to the sequence AIRMEN. 
"""

def sequence():
	# create a list to hold tuples which returns
	steps = []
	inWord = "MARINE"
	outWord = "AIRMEN"
	inWordList = list(inWord)
	# for every letter in MARINE
	# check if the corresponding letter is the one in AIRMEN
	# if not, switch the current index with the target index with neighbor transpositions, add the tuple to the list
	for i in range (0, len(inWord)):
		if not inWordList[i] == outWord[i]:
			for j in range (i+1, len(inWord)):
				if inWordList[j] == outWord[i]:
					a, b = i, j
					for k in range (0, j-i):
						inWordList[b-1], inWordList[b] = inWordList[b], inWordList[b-1]
						b = b - 1
						steps.append((b, b+1))
					for k2 in range (0, j-i-1):
						b = b + 1
						inWordList[b+1], inWordList[b] = inWordList[b], inWordList[b+1]
						steps.append((b, b+1))
	# return the list 
	return steps

print(sequence())