from collections import Counter
inp = 372037-905157

nums = list(range(372037, 905158))

str_nums = [[ch for ch in str(n)] for n in nums if len(str(n))==6]


def check(num):
    p = False
    for i in range(5):
        if num[i] > num[i+1]:
            return False
    c = Counter(num)
    for v in c.values():
        if v > 2 and 2 not in c.values():
            return False
    if 2 in c.values():
        p = True
    return True & p 

res = [s for s in split_s6 if check(s)]

len(res)


