import numpy as np
inp = open('i2.txt').readlines()

# part 1
b = np.array([[int(y) for y in x.rstrip().split('x')] for x in inp])
b = np.sort(b,axis=1)
np.sum([(3*np.product(x[[0,1]]), 2*np.product(x[[1,2]]), 2*np.product(x[[2,0]])) for x in b])


# part 2
np.sum([(2*np.sum(x[[0,1]]), np.product(x)) for x in b])
