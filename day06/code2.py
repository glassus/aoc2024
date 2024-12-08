data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

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
    
def is_free_road(pos, target, direction):
    while pos in m and pos != target:
        if m[pos] == '#':
            return False
        pos = pos + direction
    if not pos in m:
        return False
    return True

    
  
pos = start
obs = []
direction = -1j
while pos + direction in m:
    for target in lst_blocks:
        if is_free_road(pos, target, direction*1j):
            if direction in (1,-1):
                if pos.real == target.real:
                    print("pos", pos, "target", target)
                    obs.append(pos + direction)
            if direction in (1j,-1j):
                if pos.imag == target.imag:
                    print("pos", pos, "target", target)
                    obs.append(pos + direction)                      
    if m[pos + direction] != '#':
        pos = pos + direction
    else:
        direction *= 1j

print(obs)
