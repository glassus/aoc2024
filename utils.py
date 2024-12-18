from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase


def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
    return d

def affiche(space):
    for y in range(len(data)):
        for x in range(len(data[0])):
            print(space[x+y*1j], end='')
        print()

largeur = len(data[0])
hauteur = len(data)

def voisins(grid, pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid and True:
            lst.append(npos)
    return lst


import networkx as nx

G = nx.Graph()

for pos in d:
    if d[pos] == '.':
        vois = voisins(pos)
        for v in vois:
            G.add_edge(pos, v)
            
chemins = nx.all_simple_paths(G, source=start, target=end)
