import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

data = open('input.txt').read().split('\n\n')
#data = open('input_test2.txt').read().split('\n\n')

data_gates = data[0].splitlines()
data_rules = data[1].splitlines()

gates = {}
for line in data_gates:
    a, b = line.split(': ')
    gates[a] = int(b)



for line in data_rules:
    a, b = line.split(' -> ')
    c, op, d = a.split(' ')
    G.add_edge(c,d)
    G.add_edge(d,b)
    
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=12)
plt.show()
