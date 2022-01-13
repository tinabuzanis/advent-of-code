import re
from itertools import permutations

r = open('input.txt').read().strip().split('\n')
nums = [2,3,4,7]
inp = [ re.sub('^[^_]*\|',"", line) for line in r.splitlines()]
b = [''.join(line).split() for line in inp]
c = [[1 if (len(word) in nums) else 0  for word in line] for line in b]
print(sum(sum(np.array(c))))
p1 = sum(sum(np.array(c)))


d = {'acedgfb':8, 'cdfbe':5, 'gcdfa':2, 'fbcad':3, 'dab':7,'cefabd':9, 'cdfgeb':6, 'eafb':4, 'cagedb':0, 'ab':1}
d = {''.join(sorted(k)):v for k,v in d.items()}

ans = 0
for line in s:
    a,b = line.split(" | ")
    a = a.split(" ")
    b = b.split(" ")
    for perm in permutations('abcdefg'):
        p_ = {a:b for a,b in zip(perm,"abcdefg")}
        a_ = ["".join(p_[c] for c in x) for x in a]
        b_ = ["".join(p_[c] for c in x) for x in b]
        if all("".join(sorted(an)) in d for an in a_):
            b_ = ["".join(sorted(x)) for x in b_]
            ans += int("".join(str(d[x]) for x in b_))
            break
print(ans)
