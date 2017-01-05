import time

def execute(lines, registers):
    program = 0
    registers = registers.copy()
    while program < len(lines):
        i = lines[program].strip().split()
        p1 = 0
        if i[1][-1].isdigit():
            p1 = int(i[1])
        else:
            p1 = registers[i[1]]
        if i[0] == 'cpy':
            if not i[2].isdigit():
                registers[i[2]] = p1
        if i[0] == 'inc':
            registers[i[1]] += 1
        if i[0] == 'dec':
            registers[i[1]] -= 1
        if i[0] == 'tgl':
            idx = program + registers[i[1]]
            if idx >= 0 and idx < len(lines):
                inst = lines[idx].strip().split()
                if len(inst) == 2:
                    if inst[0] == 'inc':
                        inst[0] = 'dec'
                    else:
                        inst[0] = 'inc'
                else:
                    if inst[0] == 'jnz':
                        inst[0] = 'cpy'
                    else:
                        inst[0] = 'jnz'
                lines[idx] = ' '.join(inst)
        if i[0] == 'jnz' and p1 != 0:
            p2 = i[2]
            if not i[2][-1].isdigit():
                p2 = registers[i[2]]
            else:
                p2 = int(p2)
            program += p2
            continue
        program += 1
    return registers['a']

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

registers = { 'a': 7, 'b': 0, 'c': 0, 'd': 0 }
print('Problem 1:', execute(lines.copy(), registers))
t = time.process_time() - t
print("Time elapsed: {0} ms".format(t * 1000))
t = time.process_time()

registers['a'] = 12
print('Problem 2:', execute(lines.copy(), registers))
t = time.process_time() - t
print("Time elapsed: {0} s".format(t))
