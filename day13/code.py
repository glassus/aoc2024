data = open('input.txt').read().splitlines()
#ata = open('input_test.txt').read().splitlines()


from sympy import solve
from sympy.abc import x, y, z

rules = []
for i in range(0, len(data), 4):
    a, b = data[i].split(', ')
    c = int(a[len("Button A: X+"):])
    d = int(b[len("Y+"):])
    e, f = data[i+1].split(', ')
    g = int(e[len("Button A: X+"):])
    h = int(f[len("Y+"):])
    j, k = data[i+2].split(', ')
    l = int(j[len("Prize: X="):])
    m = int(k[len("Y="):])
    rules.append((c,g,l+10000000000000,d,h,m+10000000000000))
    
def make_eqs(rule):
    c,g,l,d,h,m = rule
    e1 = c*x + g*y - l
    e2 = d*x + h*y - m
    return e1, e2

def solve_eq(e1, e2):
    solutions = solve([e1,e2], x, y)
    return solutions

def is_valid(sol):
    if "/" in str(sol[x]):
       return False
    if "/" in str(sol[y]):
       return False
    return True
    

s = 0
for rule in rules:
    sol = solve_eq(*make_eqs(rule))
    if is_valid(sol):
        s += 3*sol[x] + sol[y]
print(s)
