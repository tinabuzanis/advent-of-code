ff = open('i.txt').read()

ff = ff[:-1]


ff = ff.split('\n\n')

ff = [l.replace('\n', ' ').split(' ') for l in ff]

valid_len = [l for l in ff if len(l) == 7 or len(l) == 8]

sp = [[line.split(':') for line in batch] for batch in valid_len]

sp
"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""

def pcheck(line):
    if line[0] == 'byr':
        num = int(line[1])
        if len(line[1]) != 4  or num < 1920 or num > 2002:
            return False
        
    elif line[0] == 'iyr':
        num = int(line[1])
        if len(line[0]) != 4 or num < 2010 or num > 2020:
            return False

    elif line[0] == 'eyr':
        num = int(line[1])
        if len(line[0]) != 4 or num < 2020 or num > 2030:
            return False

    elif line[0] == 'hgt':
        num = int(line[1][:-2])
        unit = line[1][-2:]
        if unit == 'cm':
            if num < 150 or num > 193:
                return False
        else:
            if num < 59 or num > 76:
                return False

    elif line[0] == 'hcl':
        if line[1] != '#' or len(line[1][1:]

            
# gg = [[line[0:3] for line in s] for s in ff]

# sum([True if len(x) == 8 or (len(x) == 7 and 'cid' not in x) else False for x in gg])

cc = "512in"

cc[:-2]
