data = open('input.txt').read().split('\n\n')
#data = open('input_test.txt').read().split('\n\n')

data = [v.splitlines() for v in data]

def convert_to_lock(lst):
    lock = [0]*5
    for i in range(1, len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#':
                lock[j] += 1
    return lock

def convert_to_key(lst):
    key = [0]*5
    for i in range(len(lst)-1):
        for j in range(len(lst[0])):
            if lst[i][j] == '#':
                key[j] += 1
    return key

locks = []
keys = []
for lst in data:
    if lst[0] == '#####':
        locks.append(convert_to_lock(lst))
    else:
        keys.append(convert_to_key(lst))
        
def match(key, lock):
    for k, l in zip(key, lock):
        if k + l > 5:
            return False
    return True

n = 0
for key in keys:
    for lock in locks:
        if match(key, lock):
            n += 1
print(n)