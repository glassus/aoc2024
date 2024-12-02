data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

data = [line.split() for line in data]
data = [[int(k) for k in lst] for lst in data]

def incr_decr(lst):
    return lst == sorted(lst) or lst[::-1] == sorted(lst)

def adj(lst):
    for i in range(len(lst)-1):
        diff = abs(lst[i+1]-lst[i])
        if diff not in (1,2,3):
            return False
    return True

def safe(lst):
    return incr_decr(lst) and adj(lst)

p1 = sum(safe(lst) for lst in data)
#print(p1)

def tolerate(lst):
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if safe(new_lst):
            return True
    return False

p2 = sum(tolerate(lst) for lst in data)
print(p2)
        