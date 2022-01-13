import numpy as np

f = open('input.txt').read().strip('\n')

# part 1
res = sum([1 if x == '(' else -1 for x in f]) 

# part 2
a = np.cumsum(np.array([1 if x == '(' else -1 for x in f]))
res = np.where(a == -1)


