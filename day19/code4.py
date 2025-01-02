
data_towels, data_goals = open('day19.txt').read().split('\n\n')
data_towels, data_goals = open('input.txt').read().split('\n\n')
#data_towels, data_goals = open('input_test.txt').read().split('\n\n')
towels = data_towels.split('\n')[0].split(', ')
goals = data_goals.split('\n')

d = {}
towels = sorted(towels, key=lambda x: len(x))

def nb_combs(goal):
    c = 0
    file = [goal]
    while file:
        tgt = file.pop()
        for t in towels:
            if tgt.startswith(t):
                next = tgt[len(t):]
                #print(next)
                if next == '':
                    return 1
                else:
                    file.append(tgt[len(t):])
    return 0

n = 0
for goal in goals:
    #print(goal)
    if nb_combs(goal) > 0:
        n += 1
print(n)