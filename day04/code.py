data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
#data = open('input_test2.txt').read().splitlines()

def compte(line):
    return line.count('XMAS') + line.count('SAMX')

def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
    return d

m = make_grid(data)
largeur = len(data[0])
hauteur = len(data)

def horizontal(pos):
    s = ''
    p = pos
    while p in m:
        s += m[p]
        p += 1
    return s

def vertical(pos):
    s = ''
    p = pos
    while p in m:
        s += m[p]
        p += 1j
    return s

def diag_desc(pos):
    s = ''
    p = pos
    while p in m:
        s += m[p]
        p += 1+1j
    return s

def diag_asc(pos):
    s = ''
    p = pos
    while p in m:
        s += m[p]
        p += 1-1j
    return s

def part1():
    s = 0
    for p in range(largeur):
        s += compte(vertical(p))
        if p != 0:
            s += compte(diag_desc(p))
            s += compte(diag_asc(p+(hauteur-1)*1j))
    for k in range(hauteur):
        s += compte(horizontal(0+k*1j))
        s += compte(diag_desc(0+k*1j))
        s += compte(diag_asc(0+k*1j))
    print(s)


def is_motif(p):  
    if (m[p], m[p+1+1j], m[p+2+2j]) not in (('M', 'A', 'S'), ('S', 'A', 'M')):
        return False    
    if (m[p+2j], m[p+1+1j], m[p+2]) not in (('M', 'A', 'S'), ('S', 'A', 'M')):
        return False     

    return True

def part2():
    s = 0
    for x in range(largeur-2):
        for y in range(hauteur-2):
            p = x + y*1j
            s += is_motif(p)
    print(s)
