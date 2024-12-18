r = {}

a = 44374556
b = 0
c = 0

p = "2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0"


p = list(map(int, p.split(',')))


def combo(n):
    if n <= 3:
        return n
    if n == 4:
        return a
    if n == 5:
        return b
    if n == 6:
        return c


def adv(i):
    global a
    a = a // (2**combo(p[i+1]))
    return i + 2

def bxl(i):
    global b
    b = b ^ p[i+1]
    return i + 2

def bst(i):
    global b
    b = combo(p[i+1]) % 8
    return i + 2

def jnz(i):
    if a != 0:
        return p[i+1]
    else:
        return i + 2

def bxc(i):
    global b
    b = b ^ c
    return i + 2

def out(i):
    print(combo(p[i+1]) % 8, end=', ')
    return i + 2

def bdv(i):
    global b
    b = a // (2**combo(p[i+1]))
    return i + 2    
        
def cdv(i):
    global c
    c = a // (2**combo(p[i+1]))
    return i + 2      

f = {0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}

i = 0
while i < len(p):
    i = f[p[i]](i)    