"""
Combination (order does not matter) and Permutation (order matters)
"""

# Rule of sum
print(['Alice', 'Bob', 'Charlie']  + [0, 1, 2, 3, 4])

# Rule of product
from itertools import product
for p in product(['a', 'b', 'c'], ['x', 'y']):
  print("".join(p))

# Tuples
for p in product("ab", repeat=3):
  print("".join(p))

# Permutations
from itertools import permutations
for p in permutations("abcd", 2):
  print("".join(p))
