r = open('input.txt').read().strip('\n')
import re
input = [[int(y) if y.isdigit() else y for y in re.split('-| |: ',line)] for line in r.splitlines()]


#Part 1
valid = 0
for entry in input:
    if entry[0] <= entry[3].count(entry[2]) <= entry[1]:
        valid = valid + 1

print(valid)

#Part 2
valid = 0
for entry in input:
    if (entry[3][entry[0]-1] == entry[2]) != (entry[3][entry[1]-1] == entry[2]):
        valid = valid + 1

print(valid)

