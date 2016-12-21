import time

t = time.process_time()

discs = []

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    args = line.strip().split()
    positions = int(args[3])
    start = int(args[-1][:-1])
    discs.append((positions, start))

p1 = -1
start_time = 0
while p1 == -1:
    found = True
    for i, disc in enumerate(discs):
        if (start_time + i + 1 + disc[1]) % disc[0] != 0:
            found = False
    if found:
        p1 = start_time
    start_time += 1

print('Problem 1:', p1)
t = time.process_time() - t
print('Elapsed time: {0} s'.format(t))
t = time.process_time()

discs.append((11, 0))
p1 = -1
while p1 == -1:
    found = True
    for i, disc in enumerate(discs):
        if (start_time + i + 1 + disc[1]) % disc[0] != 0:
            found = False
    if found:
        p1 = start_time
    start_time += 1

print('Problem 2:', p1)
t = time.process_time() - t
print('Elapsed time: {0} s'.format(t))
