data, h, w = open('input.txt').read().splitlines(), 103, 101
#data, h, w = open('input_test.txt').read().splitlines(), 7, 11
#data, h, w = ["p=2,4 v=2,-3"], 7, 11

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy


from collections import defaultdict

class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        
    def move(self):
        self.x = (self.x + self.dx) % w
        self.y = (self.y + self.dy) % h

robots = []
def parse():
    for line in data:
        a, b = line.split(' v=')
        c, d = list(map(int, a[2:].split(',')))
        e, f = list(map(int, b.split(',')))
        robots.append(Robot(c,d,e,f))
        
parse()

def affiche():
    pos = defaultdict(int)
    for r in robots:
        pos[(r.x, r.y)] += 1
    for y in range(h):
        for x in range(w):
            if pos[(x,y)] == 0:
                print('.', end='')
            else:
                print(pos[(x,y)], end='')
        print()
x = []
cs = []


for _ in range(100):
    x.append(_+1)
    p = []
    for r in robots:
        r.move()
        p.append((r.x, r.y))
    c = entropy(p, base=2)
    cs.append(c)
        
        
plt.plot(x,cs)
plt.show()


# q1, q2, q3, q4 = 0, 0, 0, 0
# mw = w//2
# mh = h//2
# for r in robots:
#     if r.x < mw and r.y < mh:
#         q1 += 1
#     if r.x > mw and r.y < mh:
#         q2 += 1
#     if r.x > mw and r.y > mh:
#         q3 += 1
#     if r.x < mw and r.y > mh:
#         q4 += 1
# print(q1*q2*q3*q4)
    