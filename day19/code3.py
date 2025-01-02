
data_towels, data_goals = open('input.txt').read().split('\n\n')
data_towels, data_goals = open('input_test.txt').read().split('\n\n')
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
    
n = 0
def parcours(a, mot):
    if a is None:
        return
    
    global n
    if mot == '':
        print("trouvé")
        n += 1
        return
    
    print("comparaison de ", mot, "avec", a.data)
    if mot.startswith(a.data):
        print(mot, ": debut", a.data, "trouvé, poursuite avec", mot[len(a.data):])
        parcours(a_origine, mot[len(a.data):])
        
        newmot = mot[len(a.data):]
        if newmot == '':
            return
#         if newmot < a.data:
#             parcours(a.left, newmot)
#         else:
#             parcours(a.right, newmot)
    if mot < a.data:
        parcours(a.left, mot)
    else:
        parcours(a.right, mot)    

parcours(a, "bbrgwb")