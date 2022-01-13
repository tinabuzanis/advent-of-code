f = open('input.txt').readlines()
f = [line.strip('\n') for line in f]

f = [int(line) for line in f]

f

a = [np.floor(x/3) - 2 for x in f]

def fuel(amt):
    fc = 0
    while(amt > 5):
        amt = np.floor(amt/3) - 2
        fc += amt
        print(amt)
    return fc

np.sum([fuel(x) for x in f])


