data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

lstA = []
lstB = []
for line in data:
    a, b = line.split()
    lstA.append(int(a))
    lstB.append(int(b))
    
lstA.sort()
lstB.sort()

s = sum([abs(a-b) for a, b in zip(lstA, lstB)])
print(s)

s = sum([elt*lstB.count(elt) for elt in lstA])
print(s)