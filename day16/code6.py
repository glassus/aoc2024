data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

import time

t0 = time.time()

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


grid, true_start, end = make_grid(data)



def shortest(grid, start, end, forbidden=None):
    file = [start]
    poids = {pos:10**9 for pos in grid if grid[pos] != '#'}
    poids[start] = 0
    parent = {}
    if start == true_start:
        parent[start] = start - 1
    else:
        parent[start] = forbidden
    #print('interdit', parent[start])
    seen = set()
    while file:
        file = sorted(file, key=lambda x:poids[x])
        curr = file.pop(0)
        seen.add(curr)
        for v in voisins(grid, curr):
            if v == parent[start]:
                continue
            score = 1
            if not are_col(v, curr, parent[curr]):
                score = 1001  
            if poids[v] > poids[curr] + score:
                poids[v] = poids[curr] + score
                parent[v] = curr
            if v not in seen:
                file.append(v)
    if end not in seen:
        return 0, 0, 0
    return poids[end], poids, parent

def remonte(grid, parent, start, end):
    path = [end]
    curr = end
    while curr != start:
        curr = parent[curr]
        path.append(curr)
    path.reverse()
    return path

score, poids, parent = shortest(grid, true_start, end)
path = remonte(grid, parent, true_start, end)

def bifurcations(path):
    lst = []
    for p in path:
        if len(voisins(grid, p)) > 2:
            lst.append(p)
    return lst

tiles = set()
tiles = tiles | set(path)

for p in bifurcations(path):
    prev = path[path.index(p)-1]
    suiv = path[path.index(p)+1]
    for v in voisins(grid, p):
        if v in path:
            continue
        score_v, poids_v, parent_v = shortest(grid, v, end, p)
        if (score_v, poids_v, parent_v) == (0, 0, 0):
            continue
        path_v = remonte(grid, parent_v, v, end)
        if not are_col(prev, p, v):
            bonus = 1001
        else:
            bonus = 1
        if score_v + poids[p] + bonus == score:
            tiles = tiles | set(path_v)
print(len(tiles))   
print(time.time()-t0)