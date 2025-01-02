
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
    
towels.sort()
start = towels[len(towels)//2]
a = Arbre(start)
a_origine = Arbre(start)

for t in towels:
    if t == start:
        continue
    a = insertion(a, t)
    a_origine = insertion(a_origine, t)
    
n = 0
def parcours(a, mot):
    
    global n
    if mot == '':
        print("trouvé")
        n += 1
        return
    while a is not None:
        print("comparaison de ", mot, "avec", a.data)
        if mot.startswith(a.data):
            print("debut", a.data, "trouvé, poursuite avec", mot[len(a.data):])
            parcours(a_origine, mot[len(a.data):])
        if mot < a.data:
            print("gauche")
            a = a.left
        else:
            print("droite")
            a = a.right
    

parcours(a, "rrbgbr")