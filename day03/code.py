data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

t = "t_mul(542,5)+mmul(548,5mul(54,25)"
t = data[0]


def compte(t):
    s = 0
    i = 0
    while i < len(t):
        while i+4 < len(t) and t[i:i+4] != 'mul(':
            i += 1
        i += 4
        if i < len(t) and t[i].isdigit():
            n1_deb = i
            while i < len(t) and t[i].isdigit():
                i += 1
            n1_end = i
            #i += 1
            if i < len(t) and t[i] == ',':
                i += 1
                if i < len(t) and t[i].isdigit():
                    n2_deb = i
                    while i < len(t) and t[i].isdigit():
                        i += 1
                    n2_end = i
                    #i += 1
                    if i < len(t) and t[i] == ')':
                        n1 = int(t[n1_deb:n1_end])
                        n2 = int(t[n2_deb:n2_end])
                        s += n1*n2
    return s


print(sum(compte(line) for line in data))