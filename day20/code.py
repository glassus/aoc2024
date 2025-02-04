data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

import networkx as nx

def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
            if d[x+y*1j] == 'S':
                start = x+y*1j
            if d[x+y*1j] == 'E':
                end = x+y*1j
    return d, start, end


# def affiche(space):
#     for y in range(h):
#         for x in range(w):
#             print(space[x+y*1j], end='')
#         print()
        
def voisins(grid, pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid and grid[npos] in '.ES':
            lst.append(npos)
    return lst

grid, start, end = make_grid(data)

def bordure(pos):
    return pos.real == 0 or \
           pos.real == len(data[0])-1 or \
           pos.imag == 0 or \
           pos.imag == len(data)-1

def voisins_cheat(grid, pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid:
            lst.append(npos)
    return lst

def set_cheat(grid):
    s = set()
    for pos in grid:
        if bordure(pos):
            continue
        for v in voisins_cheat(grid, pos):
            if not bordure(v):
                s.add((pos, v))
    return s


def calc(p1, p2):
    grid, start, end = make_grid(data)
    grid[p1] = '.'
    grid[p2] = '.'
    G = nx.Graph()
    for pos in grid:
        if grid[pos] == '.':
            vois = voisins(grid, pos)
            for v in vois:
                G.add_edge(pos, v)
    path = nx.shortest_path(G, source=start, target=end)
    return path

cheats = set_cheat(grid)

def run(save):
    tgt = 84-save
    n = 0
    seen = set()
    for (p1,p2) in cheats:
        path = calc(p1, p2)
        if len(path)-1 == tgt:
            if (p1, p2) not in seen and p1 in path and p2 in path:
                n += 1
                seen.add((p1,p2))
            
    return n, seen
