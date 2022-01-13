import numpy as np

def btod(l):
    arr = np.array(l)
    return arr.dot(2**np.arange(arr.size)[::-1])

f = open('input.txt', 'r')
a = np.array([list(map(int, list(l.rstrip()))) for l in f if len(l) > 1])

# part 1
gamma = np.array(np.mean(a, axis=0) > 0.5, dtype=int)
epsilon = np.array([not b for b in gamma], dtype=int)
print(btod(gamma) * btod(epsilon))


# part 2
ox = a.copy()
for i in range(len(ox[0])):
    b=int(np.mean(ox[:,i]) >= 0.5)
    ox = ox[ox[:,i] == b]
    if ((ox == ox[0]).all()): break;
co = a.copy()
for i in range(len(co[0])):
    b=int(np.mean(co[:,i]) < 0.5)
    co = co[co[:,i] == b]
    if ((co == co[0]).all()): break;
print(btod(ox[0])*btod(co[0]))

