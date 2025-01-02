data_towels, data_goals = open('day19.txt').read().split('\n\n')
data_towels, data_goals = open('input.txt').read().split('\n\n')
data_towels, data_goals = open('input_test.txt').read().split('\n\n')
towels = data_towels.split('\n')[0].split(', ')
goals = data_goals.split('\n')

from functools import lru_cache

@lru_cache
def nb_combs(mot):
    print(mot)
    if mot == '':
        return 1
    s = 0    
    for pref in towels:
        if mot.startswith(pref):
            sub = mot[len(pref):]
            s += nb_combs(pref)*nb_combs(sub)

    return s