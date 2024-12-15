data = open('input.txt').read().splitlines()
data = open('input_test2.txt').read().splitlines()

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
        line = expand(data[y])
        for x in range(len(line)):
            d[x+y*1j] = line[x]
            if line[x] == '@':
                start = x+y*1j
    return d, start


def expand(line):
    newline = ''
    for c in line:
        if c == '#':
            newline += '##'
        if c == 'O':
            newline += '[]'
        if c == '.':
            newline += '..'
        if c == '@':
            newline += '@.'
    return newline
    







grid, start = make_grid(data)

def affiche(space):
    for y in range(hauteur):
        for x in range(2*largeur):
            print(space[x+y*1j], end='')
        print()
        
def move(grid, start, direction):
    dic = {'^':-1j, 'v':1j, '<':-1, '>':1}
    dir = dic[direction]
    pos = start
    if direction in '<>':
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
    else:
        n = 0
        while grid[pos] != '.':
            if grid[pos] == '#':
                return grid, start
            pos = pos + dir
            n += 1
        goal = pos
        block = False
        for _ in range(n):
            if grid[goal-dir] == '[':
                if grid[goal+1] != '.':
                    print("block à droite")
                    block = True
                    break
            if grid[goal-dir] == ']':
                if grid[goal-1] != '.':
                    print("block à gauche")
                    block = True
                    break
            grid[goal] = grid[goal-dir]
            if grid[goal-dir] == '[':
                grid[goal+1] = grid[goal-dir+1]
            if grid[goal-dir] == ']':
                grid[goal-1] = grid[goal-dir-1]
            goal = goal-dir
        if block:
            return grid, start
        
        grid[start] = '.'
        if grid[start+dir+dir] == '[':
            grid[start+dir+1] = '.'
        if grid[start+dir+dir] == ']':
            grid[start+dir-1] = '.'
        return grid, start+dir
           
    

def part1():
    for car in rules:
        grid, start = move(grid, start, car)


def sum_gps(grid):
    s = 0
    for pos in grid:
        if grid[pos] == 'O':
            s += int(100*pos.imag+pos.real)
    return s
        
       
        
        
        
        
        
        
        
        
        
        
        