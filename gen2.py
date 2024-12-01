import os
import sys

NB_DOSS = 25

lst = ['{:02d}'.format(k) for k in range(1, NB_DOSS+1)]

contenu =\
"""data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()"""


def create():
    for nb in lst:
        nom_doss = "day" + nb
        os.makedirs(nom_doss, exist_ok = True)

        with open(nom_doss + '/input.txt', 'w') as f:
            f.write("")

        with open(nom_doss + '/input_test.txt', 'w') as f:
            f.write("")

        with open(nom_doss + '/code.py', 'w') as f:
            f.write(contenu)



create()