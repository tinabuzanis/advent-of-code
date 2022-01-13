import numpy as np



f = 'input.txt'

ff = open(f).read().rstrip()


def htobin(i):
    return ''.join([bin(int(h, 16))[2:].zfill(4) for h in i])


b = htobin(ff)


def decode_literal(bits):
    acc = ''
    i = 0
    while 1:
        acc += bits[i+1:i+5]
        if bits[i] == '0':
            break
        i += 5
    return i+5, int(acc, 2)


def packageLength(T):
    if isinstance(T, list):
        return sum([packageLength(ll) for ll in T])
    if not isinstance(T[3], list):
        return T[2]
    return T[2] + packageLength(T[3])


def sumVersions(T):
    if isinstance(T, list):
        return sum([sumVersions(ll) for ll in T])
    if not isinstance(T[3], list):
        return T[0]
    return T[0] + sumVersions(T[3])


def parse(bits, p, pad=0) -> list:
    if (len(bits) < 8 or p == 0):
        return []
    v = int(bits[:3], 2)
    t = int(bits[3:6], 2)
    if t == 4: # a literal
        offset, value = decode_literal(bits[6:])
        rest = bits[6+offset:]
        return [(v, t, 6+offset, value)] + parse(rest, p-1, pad)
    else:
        i = int(bits[6], 2)
        l_end = 7+11 if i else 7+15
        n = int(bits[7:l_end], 2)
        if i == 1: # we have a number of subpackets
            subp = parse(bits[l_end:], n, pad+4)
            rest = bits[l_end+packageLength(subp):]
        else: # we have a total length of the subpackets
            subp = parse(bits[l_end:l_end+n], -1, pad+4)
            rest = bits[l_end+n:]
        return [(v, t, l_end, subp)] + parse(rest, p-1, pad)


res = parse(b, -1)
print('part 1:', sumVersions(res))


op = [sum, np.prod, min, max, max, lambda x: int(x[0] > x[1]), lambda x: int(
    x[0] < x[1]), lambda x: int(x[0] == x[1])]


def evaluate(T):
    if isinstance(T, list):
        return [evaluate(t) for t in T]
    if T[1] == 4:
        return T[3]
    return op[T[1]](evaluate(T[3]))



print('part 2:', evaluate(res)[0])

