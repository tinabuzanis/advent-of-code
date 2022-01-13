import numpy as np
f = open('input.txt','r')
lines = np.array([[np.array(c.split(','), dtype=int) for c in l.split(' -> ')] for l in f.readlines()])

mat = np.zeros((np.max(lines)+1, np.max(lines)+1))

for l in [l for l in lines if l[0][1] == l[1][1]]:
    xmin = min(l[0][0], l[1][0])
    xmax = max(l[0][0], l[1][0])+1
    mat[xmin:xmax, l[0][1]] += 1
for l in [l for l in lines if l[0][0] == l[1][0]]:
    ymin = min(l[0][1], l[1][1])
    ymax = max(l[0][1], l[1][1])+1
    mat[l[0][0], ymin:ymax] += 1

print(np.sum(mat > 1)) # part 1

for l in lines:
    xdir = 1 if l[0][0] < l[1][0] else -1
    ydir = 1 if l[0][1] < l[1][1] else -1
    if (l[0][0] != l[1][0] and l[0][1] != l[1][1]): # is diagonal
        for i in range(abs(l[0][0] - l[1][0])+1):
            mat[l[0][0] + xdir*i, l[0][1] + ydir*i] +=1

print(np.sum(mat > 1)) # part 2
