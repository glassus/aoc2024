data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
from functools import lru_cache
import time
t0 = time.time()

d = {
'<v':'>',
'<>':'>>',
'<^':'>^',
'<A':'>>^',
'v<':'<',
'v>':'>',
'v^':'^',
'vA':'^>',
'>v':'<',
'><':'<<',
'>^':'<^',
'>A':'^',
'^v':'v',
'^<':'v<',
'^>':'v>',
'^A':'>',
'A^':'<',
'A>':'v',
'Av':'<v',
'A<':'v<<',
'<<':'',
'>>':'',
'^^':'',
'vv':'',
'AA':''
}

# 340A
# 586A
# 839A
# 413A
# 968A

v = {}
v['340A'] = (340, '^A<<^A>vvA>A')
v['586A'] = (586, '<^^A^Av>AvvA')
v['839A'] = (839, '<^^^Avv>A^^AvvvA')
v['413A'] = (413, '^^<<AvA>>AvA')
v['968A'] = (968, '^^^AvA<^Avvv>A')

v['029A'] = (29, '<A^A^^>AvvvA')
v['980A'] = (980, '^^^A<AvvvA>A')
v['179A'] = (179, '^<<A^^A>>AvvvA')
v['456A'] = (456, '^^<<A>A>AvvA')
v['379A'] = (379, '^A<<^^A>>AvvvA')


# 340A 22440
# 
# 586A 39848
# 
# 839A 60408
# 
# 413A 28910
# 
# 968A 67760
# 219366

@lru_cache(maxsize=None)
def gen(sch, n):
    if n == 1:
        return len(sch + 'A')
    else:
        nsch = 'A' + sch + 'A' 
        return sum(gen(d[nsch[i]+nsch[i+1]], n-1) for i in range(len(nsch)-1))
    

def test(ch, n):
    s = 0
    ch = 'A' + ch  
    for i in range(len(ch)-1):
        s += gen(d[ch[i]+ch[i+1]], n)
    return s 
    
def calc():
    s = 0
    for val in data:
        c = v[val][0] * test(v[val][1], 25)
        #print(val, c)
        s += c
    return s

print(calc())
print(time.time()-t0)
# 328058358460072 too high
# 224849049574186 too low
# nope : 236848157580172 236205899214998
# à tester : 235651303255034        