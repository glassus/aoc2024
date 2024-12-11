data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
    return d

def voisins(grid, pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid:
            lst.append(npos)
    return lst

grid = make_grid(data)



def trailhead_score(pos, discovered):
    if grid[pos] == '9' and pos not in discovered:
        discovered.add(pos)
    for v in voisins(grid, pos):
        if grid[v].isdigit() and int(grid[v]) == int(grid[pos]) + 1:
            trailhead_score(v, discovered)
    return len(discovered)



def part1():
    s = 0
    for pos in grid:
        if grid[pos] == '0':
            score = trailhead_score(pos, set())
            s += score
    print(s)


def nb_h(pos, s):
    if grid[pos] == '9' :
        s[0] += 1
    for v in voisins(grid, pos):
        if grid[v].isdigit() and int(grid[v]) == int(grid[pos]) + 1:
            nb_h(v,s)
    return s[0]


def part2():
    n = 0
    for pos in grid:
        if grid[pos] == '0':
            score = nb_h(pos, [0])
            n += score
    print(n)