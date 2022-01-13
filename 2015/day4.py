import hashlib

# inp = 'abcdef609043'
inc = 0
original_inp = 'iwrupvqb'

while(1):
    inp = original_inp + str(inc)
    h = hashlib.md5(inp.encode()).hexdigest()

    if h[:6] == '000000' : 
        print(inp)
        break


    inc += 1


print(inc)



