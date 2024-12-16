data = open('input.txt').read().splitlines()
#data = open('input_test2.txt').read().splitlines()

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



def blocks_to_move(grid, pos, dir):
    if grid[pos] == '#':
        return []
    file = [pos]
    if grid[pos] == '[':
        file.append(pos+1)
    if grid[pos] == ']':
        file.append(pos-1)
    blocks = []
    while file:
        curr = file.pop(0)
        blocks.append(curr)
        #print(blocks)
        if grid[curr+dir] == '#':
            return []  
        if grid[curr+dir] == '[':
            if curr + dir not in file:
                file.append(curr+dir)
            if curr + dir+1 not in file:
                file.append(curr+dir+1)
        if grid[curr+dir] == ']':
            if curr + dir not in file:
                file.append(curr+dir)
            if curr+ dir-1 not in file:
                file.append(curr+dir-1)
    return blocks


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
        if grid[start+dir] == '.':
            grid[start+dir] = grid[start]
            grid[start] = '.'
        else:
            blocks = blocks_to_move(grid, start, dir)
            if blocks == []:
                return grid, start
            #print(blocks)
            blocks.reverse()
            for block in blocks:
                grid[block+dir] = grid[block]
                grid[block] = '.'
            grid[start] = '.'                
        return grid, start+dir
                
                

def sum_gps(grid):
    s = 0
    for pos in grid:
        if grid[pos] in '[':
            s += int(100*pos.imag+pos.real)
    return s
        
for i, car in enumerate(rules):
    grid, start = move(grid, start, car)

        
        
        
        
        
        