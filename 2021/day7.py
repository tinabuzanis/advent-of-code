pos = open("input.txt").read().split(",")
pos = [int(p) for p in pos]


# part 1
fuel = {}
for center in range(min(pos), max(pos)):
    distances = [abs(center - pos) for pos in pos]
    fuel[center] = sum(distances)
print(fuel[min(fuel, key=fuel.get)])


def triangular_number(n):
    return n * (n + 1) // 2


# part 2
fuel = {}
for center in range(min(pos), max(pos)):
    distances = [triangular_number(abs(center - pos)) for pos in pos]
    fuel[center] = sum(distances)
print(fuel[min(fuel, key=fuel.get)])



