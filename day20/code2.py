data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

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

def gen_path():
    grid, start, end = make_grid(data)
    G = nx.Graph()
    for pos in grid:
        if grid[pos] == '.':
            vois = voisins(grid, pos)
            for v in vois:
                G.add_edge(pos, v)
    path = nx.shortest_path(G, source=start, target=end)
    return path

path = gen_path()

def dist(p1, p2):
    p = p1 - p2
    return abs(p.real) + abs(p.imag)

def search(k):
    n = 0
    for i in range(len(path)):
        for j in range(i+3, len(path)):
            dst = dist(path[i], path[j])
            if dst <= 20:
                if j - i >= k + dst:
                    n += 1
    return n
