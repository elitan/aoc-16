import time
from itertools import combinations
from collections import defaultdict

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

#Filesystem     Size    Used    Avail   Use%
lines.pop(0)
lines.pop(0)

count = 0
for c in combinations(lines, 2):
    node1, node2 = c
    args = list(map(lambda x: x[:-1], node1.split()[1:4]))
    size1, used1, avail1 = map(int, args)
    args = list(map(lambda x: x[:-1], node2.split()[1:4]))
    size2, used2, avail2 = map(int, args)

    if used1 > 0 and used1 <= avail2:
        count += 1
    if used2 > 0 and used2 <= avail1:
        count += 1
print('Problem 1:', count)
t = time.process_time() - t
print('Time elapsed: {0} s'.format(t))
t = time.process_time()

rows = defaultdict(list)
for line in lines:
    args = line.split()
    trash, x, y = args[0].split('-')
    s = '.'
    if args[2] == '0T':
        s = '_'
        print(x, y)
    elif int(args[2][:-1]) > 250:
        s = '|'
    elif y == 'y0' and x == 'x34':
        s = 'G'
    rows[y].append((x, s))
for row in sorted(rows.keys(), key=lambda x: int(x[1:])):
    print(''.join(x[1] for x in rows[row]))
print('Problem 2 (by hand):', 192)
t = time.process_time() - t
print('Time elapsed: {0} s'.format(t))
