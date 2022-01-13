import numpy as np
from itertools import combinations

with open('input.txt', 'r') as file:
    inp = np.array([int(x.strip()) for x in file.readlines()])
    
    print( np.product(np.array([s for s in combinations(inp, 3) if sum(s)==2020])))
