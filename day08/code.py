data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase

digits = '0123456789'

def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
    return d

grid = make_grid(data)
antennas = defaultdict(list)

for pos in grid:
    if grid[pos] in ascii_lowercase + ascii_uppercase + digits:
        antennas[grid[pos]].append(pos)
        
antinodes = set()
def pos_antinode(a1, a2):
    return 2*a1 - a2

def part1():
    for a in antennas:
        lst_pos = antennas[a]
        for p1 in lst_pos:
            for p2 in lst_pos:
                if p1 == p2:
                    continue
                p = pos_antinode(p1, p2)
                if p in grid:
                    antinodes.add(p)

    print(len(antinodes))


def gen_lst_antinodes(p1, p2):
    vec = p2 - p1
    k = 0
    pos = p1
    lst = []
    while pos in grid:
        lst.append(pos)
        k += 1
        pos = p1+ k*vec
    return lst


def part2():
    for a in antennas:
        lst_pos = antennas[a]
        for p1 in lst_pos:
            for p2 in lst_pos:
                if p1 == p2:
                    continue
                lst_ant = gen_lst_antinodes(p1, p2)
                for ant in lst_ant:
                    if ant in grid:
                        antinodes.add(ant)

    print(len(antinodes))