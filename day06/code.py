data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

largeur = len(data[0])
hauteur = len(data)


def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
            if data[y][x] == '^':
                start = x+y*1j
    return d, start

m, start = make_grid(data)

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

part1()

def is_free_road(pos, target, direction):
    while pos != target:
        if m[pos] == '#':
            return False
        pos = pos + direction
    return True
    
#   
# lst_blocks = []
# pos = start
# obs = []
# direction = -1j
# while pos + direction in m:
#     if len(lst_blocks) >= 3:
#         target = lst_blocks[-3]
#         if direction in (1,-1):
#             if pos.real == target.real:
#                 print("target :", target)
#                 if is_free_road(pos, target, direction*1j):
#                     obs.append(pos + direction)
#         if direction in (1j,-1j):
#             if pos.imag == target.imag:
#                 print("target :", target)
#                 if is_free_road(pos, target, direction*1j):
#                     obs.append(pos + direction)                      
#     if m[pos + direction] != '#':
#         pos = pos + direction
#     else:
#         lst_blocks.append(pos + direction)
#         direction *= 1j
# 
# print(obs)
