data = open('input.txt').read().split('\n\n')
#data = open('input_test2.txt').read().split('\n\n')

data_gates = data[0].splitlines()
data_rules = data[1].splitlines()

gates = {}
for line in data_gates:
    a, b = line.split(': ')
    gates[a] = int(b)

done = 0
seen = []
while done < len(data_rules):
    for i, line in enumerate(data_rules):
        a, b = line.split(' -> ')
        c, op, d = a.split(' ')
        if c not in gates or d not in gates or i in seen:
            continue
        if op == 'AND':
            gates[b] = gates[c] & gates[d]
        if op == 'XOR':
            gates[b] = gates[c] ^ gates[d]
        if op == 'OR':
            gates[b] = gates[c] | gates[d]
        done += 1
        seen.append(i)

lst = list(gates.keys())
lst = [l for l in lst if l[0] == 'z']
lst.sort()
m = "".join([str(gates[l]) for l in lst])
print(int(m[::-1],2))