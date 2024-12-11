data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

import matplotlib.pyplot as plt

data = "9694820 93 54276 1304 314 664481 0 4"
data = "4"
lst = list(map(int, data.split(" ")))


class Stone:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

stones = []
for i, val in enumerate(lst):    
    stones.append(Stone(val))
    if i > 0:
        stones[i-1].next = stones[i]
        stones[i].prev = stones[i-1]

stone_start = stones[0]

def split(stone):
    val = stone.val
    l = len(str(val))
    v1 = int(str(val)[:l//2])
    v2 = int(str(val)[l//2:])
    snew = Stone(v2)
    stone.val = v1
    old_next = stone.next
    stone.next = snew
    snew.next = old_next
    
def blink():
    stone = stone_start
    s = 0
    while stone != None:
        if stone.val == 0:
            stone.val = 1
            stone = stone.next
        elif len(str(stone.val)) % 2 == 0:
            split(stone)
            stone = stone.next.next
            s += 1
        else:
            stone.val *= 2024
            stone = stone.next
    return s

def affiche():
    stone = stone_start
    while stone != None:
        print(stone.val, end = ' ')
        stone = stone.next

def taille():
    s = 0
    stone = stone_start
    while stone != None:
        s += 1
        stone = stone.next
    return s

X = []
Y = []
def turn(n):
    for k in range(n):
        #print(k)
        v = blink()
        X.append(k)
        Y.append(v)
    plt.plot(X,Y)
    plt.show()


