
inp1 = ['R8','U5','L5','D3']
inp2 = ['U7','R6','D4','L4']


x=0
y = 0

def U(num, coords):
    global x, y
    y += num
    coords.append((x, y))


def D(num, coords):
    global x,y
    y -= num
    coords.append((x, y))

def R(num, coords):
    global x, y
    x += num
    coords.append((x,y))

def L(num, coords):
    global x, y
    x -= num
    coords.append((x, y))

dirs = ['L', 'R', 'U', 'D']
dd = [L, R, U, D]

d = dict(zip(dirs, dd))

def get_coords(coords, inp):
    x=0
    y =0
    for i in inp:
        d[i[0]](int(i[1:]), coords)

coords1 = []
coords2 = []
inp2
coords2
get_coords(coords1, inp1)
get_coords(coords2, inp2)
import itertools
l = itertools.product(coords1, coords2)
list(l)
coords1
coords
coords2

p2 = list(itertools.permutations(coords2, 2))
p1 = list(itertools.permutations(coords1, 2))
p2
coords1
for i in range(len(coords1)-1):
    lines1.append(coords1[i], coords[i+1])


def make_lines(coords, lines):
    for i in range(len(coords)-1):
        lines.append(LineString([coords[i], coords[i+1]]))

lines2 = []
lines1 = []
make_lines(coords1, lines1)
list(lines2)
lines2

dt = []
def check_intersect(clines):
    for f, g in clines:
        ipt = f.intersection(g)
        if(type(ipt)==Point):
            dt.append(ipt)


check_intersect(clines)


def calc_distance(ipt):
    mindist = 99999
    for i, j in enumerate(ipt):
        dist = abs(j.x + j.y)
        if dist < mindist:
            mindist = dist
            midx = i
    print(midx)
dt

calc_distance(dt)


list(dt)
import shapely
from shapely.geometry import LineString, Point

line1 = LineString([A, B])
line2 = LineString([C, D])

int_pt = line1.intersection(line2)
point_of_intersection = int_pt.x, int_pt.y

print(point_of_intersection)

clines = list(itertools.product(lines1, lines2))

l


import pyparsing as pp
direction = Word(alphas, max=1)
amt = Word(nums)

