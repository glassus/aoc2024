data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

from collections import defaultdict
rules = defaultdict(list)

updates = []
i = 0
line = data[i]
while line != '':
    a, b = list(map(int, line.split('|')))
    rules[a].append(b)
    i += 1
    line = data[i]
i += 1
while i < len(data):
    line = data[i]
    updates.append(list(map(int, line.split(','))))
    i += 1

def is_correct(lst):
    for i in range(len(lst)):
        val = lst[i]
        if val not in rules:
            continue
        for nb in rules[val]:
            if nb not in lst:
                continue
            if lst.index(nb) < i:
                return False
    return True

def mid_page_number(lst):
    mid = len(lst)//2
    return lst[mid]

def part1():
    print(sum([mid_page_number(lst) for lst in updates if is_correct(lst)]))
    
class Num:
    def __init__(self, val):
        self.val = val
    
    def __lt__(self, nb):
        if (self.val not in rules) and (nb.val not in rules):
            return self.val < nb.val

        if nb.val in rules[self.val]:
            return True
        
        if self.val in rules[nb.val]:
            return False

def part2():        
    s = 0
    for lst in updates:
        if not is_correct(lst):
            new = [Num(k) for k in lst]
            new.sort()
            s += new[len(new)//2].val        
    print(s)
