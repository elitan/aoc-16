import time

def execute(lines, registers):
    program = 0
    registers = registers.copy()
    while program < len(lines):
        i = lines[program].strip().split()
        p1 = 0
        if i[1].isdigit():
            p1 = int(i[1])
        else:
            p1 = registers[i[1]]
        if i[0] == 'cpy':
            registers[i[2]] = p1
        if i[0] == 'inc':
            registers[i[1]] += 1
        if i[0] == 'dec':
            registers[i[1]] -= 1
        if i[0] == 'jnz' and p1 != 0:
            program += int(i[2])
            continue
        program += 1
    return registers['a']

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

registers = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }
print('Problem 1:', execute(lines, registers))
t = time.process_time() - t
print("Time elapsed: {0} s".format(t))
t = time.process_time()

registers['c'] = 1
print('Problem 2:', execute(lines, registers))
t = time.process_time() - t
print("Time elapsed: {0} s".format(t))
