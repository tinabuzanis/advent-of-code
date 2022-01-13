import numpy as np
f = open('input.txt', 'r')

tirage = np.array([int(i) for i in f.readline().split(',')])
boards = np.array([[int(i) for i in l.split()]
                   for l in f.read().split('\n') if len(l)]).reshape([-1, 5, 5])

for i in range(len(tirage)):
    masked = np.isin(boards, tirage[:i])
    scores = [max([np.max(np.sum(m, axis=a)) for a in [0, 1]]) for m in masked]
    best = np.argmax(scores)
    if scores[best] == 5:
        print('part 1: ', np.sum(np.logical_not(masked)[best] * boards[best]) * tirage[i - 1])
        break
        
b = boards.copy()
for i in range(len(tirage)):
    masked = np.isin(b, tirage[:i])
    scores = np.array([max([np.max(np.sum(m, axis=a)) for a in [0, 1]]) for m in masked])
    a = b[scores != 5]
    if(len(a) == 0):
        print('part 2: ', np.sum(np.logical_not(masked)[0] * b[0]) * tirage[i-1])
        break
    b = a
    
    
