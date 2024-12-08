data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

from itertools import product

goals = []
equations = []

for line in data:
    a, b = line.split(": ")
    goals.append(int(a))
    equations.append(list(map(int,b.split(' '))))
    

def test_expr(lst, goal):
    n = len(lst) - 1
    for c in product('*+|', repeat=n):
        s = []
        for i in range(len(lst)-1):
            s.append(lst[i])
            s.append(c[i])
        s.append(lst[-1])
        if eval(s) == goal:
            return True
    return False

def eval(s):
    s.reverse()
    while len(s) > 2:
        a = int(s.pop())
        sign = s.pop()
        b = int(s.pop())
        if sign == '+':
            s.append(a+b)
        elif sign == '*':
            s.append(a*b)
        else:
            s.append(int(str(a)+str(b)))
    return s[0]
    

print(sum([goal for eq, goal in zip(equations, goals) if test_expr(eq, goal)]))