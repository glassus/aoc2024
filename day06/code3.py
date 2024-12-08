data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

largeur = len(data[0])
hauteur = len(data)


def make_grid(data):
    d = {}
    lst_blocks = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
            if data[y][x] == '^':
                start = x+y*1j
            if data[y][x] == '#':
                lst_blocks.append(x+y*1j)
    return d, start, lst_blocks

m, start, lst_blocks = make_grid(data)

def part1():
    pos = start
    seen = set()
    direction = -1j
    while pos + direction in m:
        seen.add(pos)
        if m[pos + direction] != '#':
            pos = pos + direction
        else:
            direction *= 1j
    print(len(seen)+1)
    
def test_boucle(start, direction):
    seen = set()
    seen.add((start, direction)) 
    direction = direction*1j
    pos = start  
    while pos + direction in m and (pos, direction) not in seen:
        
        if m[pos + direction] != '#':
            seen.add((pos, direction)) 
            pos = pos + direction
        else:
            direction *= 1j
    if (pos, direction) in seen:
        return True
    return False


pos = start
obs = []
direction = -1j
while pos + direction in m:
    if m[pos + direction*1j] != '#':
        if test_boucle(pos, direction):
            obs.append(pos+direction)
    if m[pos + direction] != '#':
        pos = pos + direction
    else:
        while m[pos + direction] == '#':
            direction *= 1j

#print(obs)
print(len(obs))
