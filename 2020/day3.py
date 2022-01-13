with open("i.txt") as raw_data:
    data =raw_data.read()
lines = [x for x in data.split('\n') if x]

def day3_1(right, down):
    trees, x = 0, 0
    for y in range(0, len(lines), down):
        trees += int(lines[y][x] == "#")
        x = (x + right) % len(lines[y])
    return trees

print(f"Day 3.1: {day3_1(3, 1)}")
print(f"Day 3.2: {day3_1(1, 1) * day3_1(3, 1) * day3_1(5, 1) * day3_1(7, 1) * day3_1(1, 2)}")
