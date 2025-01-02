from collections import defaultdict

data_towels, data_goals = open('input.txt').read().split('\n\n')
#data_towels, data_goals = open('input_test.txt').read().split('\n\n')
towels = data_towels.split('\n')[0].split(', ')
goals = data_goals.split('\n')[:-1]

#towels = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
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
    #d[t] = init(t)
    d[t] = 1


def lst_start(mot, d):
    lst = []
    for t in d:
        if mot.startswith(t):
            lst.append(t)
    return lst


vus = {}
def nb(mot):
    if mot in vus:
        return vus[mot]
    if mot == '':
        return 1
    lst = lst_start(mot, d)
    s = 0
    for t in lst:
        sub = mot[len(t):]
        s += d[t]*nb(sub)
    vus[mot] = s
    return s
        
n = 0
for mot in goals:
    #print(mot, nb(mot))
    n += nb(mot)
print(n)
        
        
        
        
    