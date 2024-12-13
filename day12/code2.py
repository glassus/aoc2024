data = open('input.txt').read().splitlines()
#data = open('input_test3.txt').read().splitlines()
from shapely import  *
from testshapely import *

from collections import defaultdict

def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
    return d

def voisins(grid, pos, car):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid and grid[npos] == car:
            lst.append(npos)
    return lst

grid = make_grid(data)

def zone(pos):
    seen = set()
    club = [pos]
    seen.add(pos)
    pile = [pos]
    car = grid[pos]
    bords = 0
    while pile:
        curr = pile.pop()
        for v in voisins(grid, curr, car):
            bords += 1
            if v not in seen:     
                club.append(v)             
                pile.append(v)
            seen.add(v)
    return club, len(club), len(club)*4 - bords

d = defaultdict(list)
def parcours():
    vus = []
    for pos in grid:
        if pos in vus:
            continue
        club, aire, perimetre = zone(pos)
        vus = vus + club
        d[grid[pos]].append((aire, club))

parcours()

def part1():
    s = 0
    for c in d:
        lst = d[c]
        for a, p in lst:
            s += a*p
    print(s)



s = 0
for let in d:
    for aire, lst in d[let]:
        #print(lst)
        #print(nb_cotes(lst))
        s += aire*nb_cotes(lst)
print(s)
        
