data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def make_grid(data):
    d = {}
    lst_blocks = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
            if data[y][x] == '^':
                start = x+y*1j
    return d, start

m, start = make_grid(data)

obstacles = []
def is_boucle(m, start):
    pos = start
    seen = set()
    direction = -1j
    while pos in m:
        if (pos, direction) in seen:
            return True
        seen.add((pos, direction))
        while pos + direction in m and m[pos + direction] == '#':
            direction *= 1j
        pos = pos + direction
    return False

#2123 too low

def part2():
    s = 0
    m, start = make_grid(data)
    for i, pos in enumerate(m):
        if i % 100 == 0:
            print(i)
        m, start = make_grid(data)
        if pos != start:
            m[pos] = '#'
            if is_boucle(m, start):
                obstacles.append(pos)
                s += 1
    print(s)
            


part2()