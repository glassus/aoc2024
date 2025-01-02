data = open('input.txt').read().splitlines()
#data = open('input_test2.txt').read().splitlines()

data = list(map(int, data))

def mix(secret, value):
    return value^secret

def prune(secret):
    return secret % 16777216

def suiv(n):
    n = prune(mix(n, n * 64))
    n = prune(mix(n, n // 32))
    n = prune(mix(n, n * 2048))    
    return n

def part1():
    s = 0
    for n in data:
        for _ in range(2000):
            n = suiv(n)
        s += n
    print(s)

def make_last(n):
    lst = []
    for _ in range(2000):
        lst.append(n%10)
        n = suiv(n)
    return lst

def make_diff(lst):
    return [lst[i] - lst[i-1] for i in range(1, len(lst))]

def gen_diff(n):
    lst = make_last(n)
    return make_diff(lst)

def search(lst, pattern):
    i = 0

    while i + 3 < len(lst):
        if lst[i] != pattern[0]:
             i = i + 1
             continue
        if lst[i+1] != pattern[1]:
             i = i + 1
             continue
        if lst[i+2] != pattern[2]:
             i = i + 1
             continue
        if lst[i+3] != pattern[3]:
             i = i + 1
             continue
        return i+4
    
    return 0
        


def gen_best(seed, val_cible):
    lasts = make_last(seed)
    lst = [i for i in range(len(lasts)) if lasts[i] == val_cible]
    bests = []
    for i in lst:
        if i > 3:
            seq = [lasts[i-3]-lasts[i-4], lasts[i-2]-lasts[i-3],\
                   lasts[i-1]-lasts[i-2], lasts[i]-lasts[i-1]]
            bests.append((lasts[i], seq))
    return bests

tab_val = [make_last(n) for n in data]
tab_diffs = [gen_diff(n) for n in data]

maxi = 0
for n in data:
    cpl = gen_best(n, 9)
    M = 0
    for _, fen in cpl:
        s = 0
        for i, tab in enumerate(tab_diffs):
            k = search(tab, fen)
            if k != 0:
                m = tab_val[i][k]
                s += m
        if s > M:
            fenetre = fen
            M = s
    print(M)
    if M > maxi:
        maxi = M





