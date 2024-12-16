data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

import networkx as nx

def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
            if data[y][x] == 'S':
                start = x+y*1j
            if data[y][x] == 'E':
                end = x+y*1j
    return d, start, end

def voisins(grid, pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid and grid[npos] in '.ES':
            lst.append(npos)
    return lst

def are_col(a, b, c):
    u = (b.real-a.real, b.imag-a.imag)
    v = (c.real-b.real, c.imag-b.imag)
    
    return u[0]*v[1] == u[1]*v[0]


grid, start, end = make_grid(data)


G = nx.Graph()
for pos in grid:
    if grid[pos] != '#':
        vois = voisins(grid, pos)
        for v in vois:
            G.add_edge(pos, v)



file = [start]
poids = {pos:10**9 for pos in grid if grid[pos] != '#'}
poids[start] = 0
parent = {}
parent[start] = start - 1
seen = set()
while file:
    file = sorted(file, key=lambda x:poids[x])
    curr = file.pop(0)
    seen.add(curr)
    for v in voisins(grid, curr):
        score = 1
        if not are_col(v, curr, parent[curr]):
            score = 1001  
        if poids[v] > poids[curr] + score:
            poids[v] = poids[curr] + score
            parent[v] = curr
        if v not in seen:
            file.append(v)

path = [end]
curr = end
while curr != start:
    curr = parent[curr]
    path.append(curr)
path.reverse()

tiles = set(path)
bifurcations = [pos for pos in path if len(voisins(grid, pos))>2]
for i in range(len(bifurcations)-1):
    a = bifurcations[i]
    b = bifurcations[i+1]
    len_target = len(path[path.index(a):path.index(b)])
    for ch in nx.all_simple_paths(G, source=a, target=b):
        if len(ch) == len_target:
            for p in ch:
                tiles.add(p)



print(poids[end])