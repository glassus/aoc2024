from functools import lru_cache
data_towels, data_goals = open('input.txt').read().split('\n\n')
data_towels, data_goals = open('input_test.txt').read().split('\n\n')
towels = data_towels.split('\n')[0].split(', ')
goals = data_goals.split('\n')


from collections import defaultdict


d = defaultdict(lambda: 1)
for t in towels:
    d[t] = 1

mot = "rrbgbr"
p = 1
def nb(mot):
    if mot in d:
        return d[mot]
    if len(mot) == 1 and mot not in d:
        return 0
    s = 0
    for i in range(1,len(mot)-1):
        p1 = mot[:i]
        p2 = mot[i:]
        if p1 in d and p2 in d:
            s += d[p1] * d[p2]
        elif p1 in d and p2 not in d:
            s += d[p1] * nb(p2)
        elif p1 not in d and p2 in d:
            s += nb(p1) * d[p2]
        else:  
            s += nb(p1) * nb(p2)
    d[mot] = s
    return s
            
    