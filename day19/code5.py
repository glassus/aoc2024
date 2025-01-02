



from functools import lru_cache
data_towels, data_goals = open('input.txt').read().split('\n\n')
#data_towels, data_goals = open('input_test.txt').read().split('\n\n')
towels = data_towels.split('\n')[0].split(', ')
goals = data_goals.split('\n')


class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def affiche(self, indent = 0):
        val = self.data
        s = ' '*2*indent + '|' + '_' + str(val) + '\n'
        if self.left is not None:
            s += self.left.affiche(indent + 1)
        if self.left is None and self.right is not None:
            s += ' '*(2*indent+2) + '|' + '_' + 'None' + '\n'     

        if self.right is not None:
            s += self.right.affiche(indent + 1)
        if self.right is None and self.left is not None:
            s += ' '*(2*indent+2) + '|' + '_' + 'None' + '\n'  
        return s


def insertion(arbre, cle):
    if arbre is None :
        return Arbre(cle)
    else :
        val = arbre.data
        if cle <= val :
            arbre.left = insertion(arbre.left, cle)
        else:
            arbre.right = insertion(arbre.right, cle)
        return arbre
    
towels = sorted(towels, key=lambda x: len(x))
start = towels[0]
a = Arbre(start)
a_origine = Arbre(start)

for t in towels:
    if t == start:
        continue
    a = insertion(a, t)
    a_origine = insertion(a_origine, t)

def nb(mot):
    n = [0]
    @lru_cache
    def parcours(a, mot):
        if a is None:
            return
        
        
        if mot == '':
            n[0] += 1
            #print(n[0])
            return
        
        if mot.startswith(a.data):
            parcours(a_origine, mot[len(a.data):])

        if mot < a.data:
            parcours(a.left, mot)
        else:
            parcours(a.right, mot)    

    parcours(a, mot)
    return n[0]

s = 0
for i, goal in enumerate(goals[:-1]):
    print(i, goal, nb(goal))
    s += nb(goal)
#print("-"*5)
print(s)