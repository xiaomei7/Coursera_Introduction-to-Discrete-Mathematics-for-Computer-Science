from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBL", 4):
    print("".join(c))