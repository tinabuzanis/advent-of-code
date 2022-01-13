lines = list(map(int, open("_input.txt")))
count = lambda x: sum(lhs < rhs for (lhs, rhs) in zip(lines[:-x], lines[x:]))
print(count(1), count(3))
