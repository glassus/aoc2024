
data_towels, data_goals = open('day19.txt').read().split('\n\n')
data_towels, data_goals = open('input.txt').read().split('\n\n')
data_towels, data_goals = open('input_test.txt').read().split('\n\n')
towels = data_towels.split('\n')[0].split(', ')
goals = data_goals.split('\n')

from collections import defaultdict
d = defaultdict(int)



def init(goal):
    c = 0
    file = [goal]
    while file:
        tgt = file.pop()
        for t in towels:
            if tgt.startswith(t):
                next = tgt[len(t):]
                #print(next)
                if next == '':
                    c += 1
                else:
                    file.append(tgt[len(t):])
    return c


for t in towels:
    d[t] = init(t)

def nb_combs(mot):
    s = 0
    if mot in d:
        print(mot)
        return d[mot]
    if mot == '':
        return 1
    lst = list(d.keys())
    for pref in lst:
        if pref == mot:
            continue
        if mot.startswith(pref):
            sub = mot[len(pref):]
            if nb_combs(sub) != None:
                s += d[pref]*nb_combs(sub)
    d[mot] = s
    return s

print(nb_combs("brb"))