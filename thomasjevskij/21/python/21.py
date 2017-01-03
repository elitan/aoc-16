import time
from collections import deque
from itertools import permutations

def scramble(lines, password):
    for line in lines:
        if line.startswith('swap position'):
            x = int(line.split()[2])
            y = int(line.strip().split()[-1])
            s = ''
            for i in range(len(password)):
                if i == x:
                    s += password[y]
                elif i == y:
                    s += password[x]
                else:
                    s += password[i]
            password = s
            continue
        if line.startswith('swap letter'):
            x = line.split()[2]
            y = line.strip().split()[-1]
            s = ''
            for c in password:
                if c == x:
                    s += y
                elif c == y:
                    s += x
                else:
                    s += c
            password = s
            continue
        if line.startswith('rotate based'):
            x = line.strip()[-1]
            idx = password.find(x)
            idx += int(idx >= 4) + 1
            s = deque(password)
            s.rotate(idx)
            password = ''.join(s)
            continue
        if line.startswith('rotate'):
            direction = 1
            if line.split()[1] == 'left':
                direction *= -1
            x = int(line.split()[2]) * direction
            s = deque(password)
            s.rotate(x)
            password = ''.join(s)
            continue
        if line.startswith('reverse'):
            x = int(line.split()[2])
            y = int(line.strip().split()[-1]) + 1
            password = password[:x] + ''.join(reversed(password[x:y])) + password[y:]
            continue
        if line.startswith('move'):
            x = int(line.split()[2])
            y = int(line.strip().split()[-1])
            s = list(password)
            s.insert(y, s.pop(x))
            password = ''.join(s)
            continue
    return password

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

print('Problem 1:', scramble(lines, 'abcdefgh'))
t = time.process_time() - t
print('Time elapsed: {0} ms'.format(int(t * 1000)))
t = time.process_time()
for c in permutations('abcdefgh'):
    s = ''.join(c)
    if scramble(lines, s) == 'fbgdceah':
        print('Problem 2:', s)
        t = time.process_time() - t
        print('Time elapsed: {0} s'.format(t))
        break
