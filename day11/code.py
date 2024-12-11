data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

from collections import defaultdict

d = defaultdict(int)

data = "9694820 93 54276 1304 314 664481 0 4"
#data = "125 17"
#data = "15"
lst = list(map(int, data.split(" ")))

for s in lst:
    d[s] = 1

print(d)

def split(val, n):
    l = len(str(val))
    v1 = int(str(val)[:l//2])
    v2 = int(str(val)[l//2:])
    return (v1, v2, n)


def blink():
    to_add = []
    for s in d:
        if d[s] != 0:
            if s == 0:
                to_add.append((1, d[s]))
                d[0] = 0
            elif len(str(s)) % 2 == 0:
                v1, v2, n = split(s, d[s])
                to_add.append((v1, n))
                to_add.append((v2, n))
                d[s] = 0
            else:
                ns, n = s*2024, d[s]
                to_add.append((ns, n))
                d[s] = 0
    for s, n in to_add:
        d[s] += n
    #print(d)

def turn(n):
    for k in range(n):
        blink()
        
    print(sum([d[s] for s in d]))


