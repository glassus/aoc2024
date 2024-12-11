data = open('day9.txt').read()
#data = open('input_test.txt').read().splitlines()

line = data
#line = "2333133121414131402"

#line = "12345"


def gen_blocks(line):
    s = []
    i = 0
    id = 0
    while i < len(line):
        if i % 2 == 0:
            for _ in range(int(line[i])):
                s.append(id)
            id += 1
        else:
            for _ in range(int(line[i])):
                s.append('.')
            
        i += 1
    return s

def defrag(ch):
    id_block = 0
    id_file = len(ch)-1
    while id_block < id_file:
        if ch[id_block] != '.':
            id_block += 1
            continue
        if ch[id_file] == '.':
            id_file -= 1
            continue
        ch[id_block], ch[id_file] = ch[id_file], ch[id_block]
        id_block += 1
        id_file -= 1
    return ch

def checksum(ch):
    return sum([i*int(val) for i, val in enumerate(ch) if val != '.'])

def part1():
    ch = gen_blocks(line)
    ch = defrag(ch)
    #print("".join(ch))
    print(checksum(ch))


def defrag2(lst):
    id_block = 0
    id_file = len(lst)-1
    while 0 < id_file:
        if lst[id_block] != '.':
            id_block += 1
            continue
        if lst[id_file] == '.':
            id_file -= 1
            continue
        
        id_target = id_file
        nb_same_id = 0
        while lst[id_file - nb_same_id] == lst[id_target]:
            nb_same_id += 1
        
        i_dots = 0
        while i_dots < id_file:
            nb_dots = 0
            while lst[i_dots + nb_dots] == '.':
                #print("ok")
                nb_dots += 1
            if nb_dots >= nb_same_id:
                id_block = i_dots
                #print("id_block trouvé", id_block)
                break
            i_dots += 1
            
        if nb_same_id <= nb_dots:
            for i in range(nb_same_id):
                lst[id_block + i], lst[id_file-i] = lst[id_file-i], lst[id_block + i]
            id_block += nb_same_id
            id_file -= nb_same_id
        else:
            id_file -= nb_same_id    
        #print("".join([str(k) for k in lst]), "id_block", id_block, "id_file :", id_file)
        
    return lst

def part2():
    lst = gen_blocks(line)
    lst = defrag2(lst)
    with open("liste_B2.txt", 'w') as f:
        f.write(str(lst))
    #print("".join([str(k) for k in lst]))

    print(checksum(lst))

part2()