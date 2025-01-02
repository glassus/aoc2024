data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
from collections import defaultdict


d = defaultdict(list)
for line in data:
    a, b = line.split('-')
    d[a].append(b)
    d[b].append(a)
    

tr = set()
for a in d: 
    for b in d[a]:
        if b == a:
            continue
        for c in d[b]:
            if c in (a, b):
                continue
            for e in d[c]:
                if e in (c,b):
                    continue
                if e == a:
                    tr.add(tuple(sorted([a,b,c])))
n = 0
for a, b, c in tr:
    if "t" in (a[0], b[0], c[0]):
        n += 1
print(n)
        

        