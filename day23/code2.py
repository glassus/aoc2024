data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
from collections import defaultdict
import networkx as nx

G = nx.Graph()

d = defaultdict(list)
for line in data:
    a, b = line.split('-')
    G.add_edge(a,b)
    
lst = list(nx.find_cliques(G))
    
m = sorted(lst, key=len)[-1]
m.sort()
print(",".join(m))