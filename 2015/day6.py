from ast import literal_eval

import numpy as np

def day6_1():
    with open('i6.txt', 'r') as input:
        instructions = [line.split() for line in input]
    
    lights = np.zeros(shape=(1000,1000), dtype=np.int64)
    
    for instruction in instructions:
        x1, y1 = literal_eval(instruction[-3])
        x2, y2 = literal_eval(instruction[-1])
        
        if instruction[0] == 'toggle':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x,y] = abs(lights[x,y] - 1)  # flip 1 <-> 0
        
        elif instruction[1] == 'on':
            lights[x1:x2+1:1,y1:y2+1:1] = 1
        
        elif instruction[1] == 'off':
            lights[x1:x2+1:1,y1:y2+1:1] = 0
        
    print('Part 1: {} lights on'.format(np.count_nonzero(lights)))

def day6_2():
    with open('i6.txt', 'r') as input:
        instructions = [line.split() for line in input]
    
    lights = np.zeros(shape=(1000,1000), dtype=np.int64)
    
    for instruction in instructions:
        x1, y1 = literal_eval(instruction[-3])
        x2, y2 = literal_eval(instruction[-1])
        
        if instruction[0] == 'toggle':
            lights[x1:x2+1:1,y1:y2+1:1] += 2
        
        elif instruction[1] == 'on':
            lights[x1:x2+1:1,y1:y2+1:1] += 1
        
        elif instruction[1] == 'off':
            lights[x1:x2+1:1,y1:y2+1:1] -= 1
            lights[lights < 0] = 0  # stop at 0
    
    print('Part 2: {} total brightness'.format(lights.sum()))

if __name__ == "__main__":
    day6_1()
    day6_2()

