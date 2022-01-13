"""

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""
f = open('i5.txt').readlines()



## ───────────────────────────────────── ▼ ─────────────────────────────────────
# {{{                           --     Part 1     --
#···············································································
ff = f[:10]


vl = ['a', 'e', 'i', 'o', 'u']
bs = ['ab', 'cd', 'pq', 'xy']

# inp = 'ugknbfddgicrmopn'


def eval_inp(inp):
    double_check = False
    vowels = False
    bad_strings = False

    if (any(map(inp.__contains__, bs))): return False

    # ss = set([inp[i:i+2] for i in range(len(inp)-2)])
    # if (ss.isdisjoint(bs) == False): 
        # print("BAD STRING")
        # return False



# any(map(string.__contains__, substring_list))

    d = dict.fromkeys(vl, 0)

    for x in inp:
        if x in vl:
            d[x] += 1




    for i, x in enumerate(inp[:-1]):

        if x == inp[i+1]:
            double_check = True

    if sum(d.values()) >= 3:
        vowels = True


    # print(double_check, vowels, sum(d.values()), inp, (double_check and vowels))

    return double_check and  vowels

        # ss = [x[i:i+2] for i in range(len(x)-2)]
    # dc = [len(set(s)) for s in ss]
    # if 1 in dc:


#                                                                            }}}
## ─────────────────────────────────────────────────────────────────────────────


res = [1 if (eval_inp(inp.strip('\n'))) else 0 for inp in f] 

sum(res)

from collections import Counter

## ───────────────────────────────────── ▼ ─────────────────────────────────────
# {{{                          --     Part 2     --
#···············································································
def eval_inp(inp):
    double_check = False
    pal = False

    tmp = ""
    ct = 0
    bad_string = []

    for i in inp:
        print(i, tmp, ct)
        if i == tmp:
            ct += 1

            if ct == 2:
                bad_string.append(i*2)
                ct = 0
                tmp = ""
        else:
            tmp = i
            ct = 0

    sp = [inp[i:i+2] for i in range(len(inp)- 1)]
    st = [inp[i:i+3] for i in range(len(inp) - 2)]

    sc = Counter(sp)
    for k,  v in sc.items():
        if v > 1 and k not in bad_string:
            double_check = True


    for s in st:
        if s[0] == s[2]:
            pal = True

    print(double_check, pal, inp, double_check and pal)

    return double_check and pal
#                                                                            }}}
## ─────────────────────────────────────────────────────────────────────────────

eval_inp('xilodxfuxphuiiii')

res = [inp.strip('\n') if (eval_inp(inp.strip('\n'))) else 0 for inp in f] 
sum(res)

inp = 'xxyxx'
inp = 'aaaxa'

    print(i, tmp, ct)

bad_string

k = 'aa'

k not in bad_string

sc = Counter(sp)
sp = [inp[i:i+2] for i in range(len(inp) -1)]

sp

sc = Counter(sp)

for k, v in sc.items():
    if v > 1 and k in bad_string:
        print("YAY")



for i, x in range(enumerate(inp)-a
sp = [inp[i:i+2] for i in range(0, len(inp) -1)]

sp = inp[::2]

sp

sc = Counter(sp)

print(sc.keys(), sc.values())
for k, v in sc.items():
    if v > 1:
        print(k[0], k[1])



st = [inp[i:i+3] for i in range(len(inp) -2)]
st




check_list = []

## ───────────────────────────────────── ▼ ─────────────────────────────────────
# {{{                             --          --
#···············································································
input_string = open('i5.txt').read()
if input_string[-1] == '\n':
    input_string = input_string[:-1]

def is_nice(s):
    vowels = 0
    for c in s:
        if c in 'aeiou':
            vowels += 1
        if vowels >= 3:
            break
    if vowels < 3:
        return False
    repeat = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeat = True
            break
    if not repeat:
        return False
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    return True

def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            # print("{} is really nice and repeats with {}".format(s, sub))
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second

count1 = 0
count2 = 0
for s in input_string.split('\n'):
    if is_nice(s):
        count1 += 1
    if is_really_nice(s):
        count2 += 1
        check_list.append(s)
print(count1)
print(count2)
#                                                                            }}}
## ─────────────────────────────────────────────────────────────────────────────
check_list

res = filter(lambda x: x !=0, res)

list(res)
