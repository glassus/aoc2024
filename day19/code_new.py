from collections import defaultdict

# data_towels, data_goals = open('input.txt').read().split('\n\n')
# data_towels, data_goals = open('input_test.txt').read().split('\n\n')
# towels = data_towels.split('\n')[0].split(', ')
# goals = data_goals.split('\n')

towels = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
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


def lst_start(mot, d):
    lst = []
    for t in d:
        if mot.startswith(t):
            lst.append(t)
    lst = sorted(lst, key=lambda x:len(x))
    return lst



def nb(mot):
    if mot in d:
        return d[mot]
    if mot == '':
        return 1
    lst = lst_start(mot, d)
    if lst == []:
        return 0
    else:
        t = lst[-1]
    sub = mot[len(t):]
    d[mot] = d[t]*nb(sub)
    return d[mot]
        
        
        
print(nb('gbr'))      
        
        
        
        
    