from shapely import  *


def carre(pos):
    x = pos.real
    y = pos.imag
    coords = [(x,y), (x+1,y), (x+1,y+1), (x,y+1)]
    return Polygon(coords)

p = [carre(0), carre(1), carre(1j), carre(2j), carre(2), carre(2j+1), carre(2+1j), carre(2j+2)]


def create_lst_pol(lst):
    s = []
    for pos in lst:
        s.append(carre(pos))
    return s


def are_col(a, b, c):
    u = (b[0]-a[0], b[1]-a[1])
    v = (c[0]-a[0], c[1]-a[1])
    
    return u[0]*v[1] == u[1]*v[0]


def nb_sides(lst):
    n = len(lst)
    s = 0
    for i in range(n):
        #print(i, (i+1)%n, (i+2)%n)
        #print(lst[i], lst[(i+1)%n], lst[(i+2)%n])
        if not are_col(lst[i], lst[(i+1)%n], lst[(i+2)%n]):
            #print("not col")
            s += 1
    return s

#t = [1j, (1+1j), 2j, (1+2j)]
#t = [0j, (1+0j), (2+0j), (3+0j)]
t = [0j, (1+0j), 1j, (1+1j), 2j, (1+2j), 3j, 4j, 5j, (1+5j), (2+5j), (3+5j), (4+5j), (3+4j), (4+4j), (3+3j), (4+3j), (5+3j), (5+4j), (5+2j), (5+1j), (5+0j), (4+0j), (3+0j), (2+0j), (2+1j), (2+2j), (5+5j)]


lst_pol = create_lst_pol(t)
p = simplify(unary_union(lst_pol), 0.01, preserve_topology=True)
s = 0
ext = list(p.exterior.coords)[:-1]
s += nb_sides(ext)
if len(p.interiors) > 0:
    for i in range(len(p.interiors)):
        inte = list(p.interiors[i].coords)[:-1]
        s += nb_sides(inte)
print(s)

