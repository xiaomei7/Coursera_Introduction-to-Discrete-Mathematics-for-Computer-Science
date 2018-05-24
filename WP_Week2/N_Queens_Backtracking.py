def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n, numSolution):
    if len(perm) == n:
        numSolution.append(1);
        print(perm)
        #exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n, numSolution)
            # removes and returns the last item in the list
            perm.pop()

numSolution = [];
extend([], 8, numSolution)
print(len(numSolution))

