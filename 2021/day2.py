horizontal = depth = aim =  0

with open('input.txt', 'r') as file:
    for line in file:
        match line.split():
            case 'forward', X:
                horizontal += int(X)
                depth += aim * int(X)
            case 'down', X:
                 # depth += int(X)
                aim += int(X)
            case 'up', X:
                # depth -=int(X) 
                aim -= int(X)

print(horizontal * depth)



