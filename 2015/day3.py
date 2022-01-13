from collections import defaultdict

d = defaultdict(int)
x  = [0,0]
y = [0,0]
a = b = 0


inp = open('i3.txt').read().rstrip()

d[(a,b)] =1
count = 0

for i in inp:
    s = count % 2

    if i == '^':
        y[s]+=1
        b = y[s]

    elif i == 'v':
        y[s] -= 1
        b = y[s]

    elif i == '<':
        x[s] -= 1
        a =  x[s]

    elif i == '>':
        x[s] += 1
        a = x[s]

    else:
        print(i)

    d[(x[s],y[s])] += 1
    count += 1


sum([1 for k, v in d.items() if v > 0])


