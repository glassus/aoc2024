import networkx as nx

G = nx.Graph()

d = {}
d['0'] = 1
d['A'] = 2
d['1'] = 1j
d['2'] = 1j+1
d['3'] = 1j+2
d['4'] = 2j
d['5'] = 2j+1
d['6'] = 2j+2
d['7'] = 3j
d['8'] = 3j+1
d['9'] = 3j+2

G.add_edge(d['0'], d['A'])
G.add_edge(d['0'], d['2'])
G.add_edge(d['2'], d['3'])
G.add_edge(d['2'], d['1'])
G.add_edge(d['2'], d['5'])
G.add_edge(d['1'], d['4'])
G.add_edge(d['3'], d['6'])
G.add_edge(d['4'], d['5'])
G.add_edge(d['4'], d['7'])
G.add_edge(d['5'], d['8'])
G.add_edge(d['5'], d['6'])
G.add_edge(d['7'], d['8'])
G.add_edge(d['8'], d['9'])
G.add_edge(d['6'], d['9'])
G.add_edge(d['3'], d['A'])

lst = list(nx.all_shortest_paths(G, d['A'], d['4']))

go = {-1:'<', 1:'>', -1j:'v', 1j:'^'}

def gen_ch(lst):
    s = ''
    for i in range(len(lst)-1):
        s += go[lst[i+1]-lst[i]]
    return s

def gen_lst(s):
    s = 'A' + s
    mvts = []
    for i in range(len(s)-1):
        lst = list(nx.all_shortest_paths(G, d[s[i]], d[s[i+1]]))
        mvts.append([gen_ch(l) for l in lst])
    return mvts

def gen_all_strings(s):
    all_s = ['']
    mvts = gen_lst(s)
    for mvt in mvts:
        to_add = []
        for m in mvt:
            for ch in all_s:
                ch += m + 'A'
                to_add.append(ch)
        all_s = to_add.copy()
    return all_s

