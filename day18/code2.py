data, w, h = open('input.txt').read().splitlines(), 71, 71
#data, w, h = open('input_test.txt').read().splitlines(), 7, 7
import networkx as nx
import time

t0 = time.time()

def parse(i):
    lst_pos = []
    for line in data[:i]:
        a, b = list(map(int, line.split(',')))
        lst_pos.append((a,b))
    return lst_pos

def make_grid(i):
    lst_pos = parse(i)
    d = {}
    for y in range(h):
        for x in range(w):
            if (x,y) in lst_pos:
                d[x+y*1j] = '#'
            else:
                d[x+y*1j] = '.'
    return d

#grid = make_grid(data[:1024])
start = 0
end = (w-1) + (h-1)*1j

def affiche(space):
    for y in range(h):
        for x in range(w):
            print(space[x+y*1j], end='')
        print()


def voisins(grid, pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid and grid[npos] == '.':
            lst.append(npos)
    return lst

i = 2995
a = 0
b = len(data)
while True:
    if a > b:
        print(data[m])
        break
    m = (a+b)//2
    grid = make_grid(m)
    
    G = nx.Graph()

    for pos in grid:
        if grid[pos] == '.':
            vois = voisins(grid, pos)
            for v in vois:
                G.add_edge(pos, v)
    try:            
        c = nx.shortest_path(G, source=start, target=end)
        a = m + 1
    except:
        b = m -1
print(time.time()-t0)    