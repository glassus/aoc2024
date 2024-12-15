data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

lim = 0
while data[lim] != '':
    lim += 1

largeur = len(data[0])
hauteur = lim

rules = ""
for i in range(lim+1, len(data)):
    rules += data[i]

def make_grid(data):
    d = {}
    for y in range(hauteur):
        for x in range(largeur):
            d[x+y*1j] = data[y][x]
            if data[y][x] == '@':
                start = x+y*1j
    return d, start

grid, start = make_grid(data)

def affiche(space):
    for y in range(hauteur):
        for x in range(largeur):
            print(space[x+y*1j], end='')
        print()
        
def move(grid, start, direction):
    dic = {'^':-1j, 'v':1j, '<':-1, '>':1}
    dir = dic[direction]
    pos = start
    n = 0
    while grid[pos] != '.':
        if grid[pos] == '#':
            return grid, start
        pos = pos + dir
        n += 1
    goal = pos
    for _ in range(n):
        grid[goal] = grid[goal-dir]
        goal = goal-dir
    grid[start] = '.'
    return grid, start+dir
    
for car in rules:
    grid, start = move(grid, start, car)


def sum_gps(grid):
    s = 0
    for pos in grid:
        if grid[pos] == 'O':
            s += int(100*pos.imag+pos.real)
    return s
        
print(sum_gps(grid))        
        
        
        
        
        
        
        
        
        
        
        