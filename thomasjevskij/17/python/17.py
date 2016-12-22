import time, hashlib
from collections import deque

def explore_node(node):
    added = []
    xy, passcode = node
    x, y = xy
    m = hashlib.md5()
    m.update(passcode.encode('utf-8'))
    s = m.hexdigest()[:4]
    if s[0] in 'bcdef' and y > 0:
        new_node = ((x, y - 1), passcode + 'U')
        added.append(new_node)
    if s[1] in 'bcdef' and y < 3:
        new_node = ((x, y + 1), passcode + 'D')
        added.append(new_node)
    if s[2] in 'bcdef' and x > 0:
        new_node = ((x - 1, y), passcode + 'L')
        added.append(new_node)
    if s[3] in 'bcdef' and x < 3:
        new_node = ((x + 1, y), passcode + 'R')
        added.append(new_node)
    return sorted(added, key=lambda x: sum(x[0]))#, reverse=True)

t = time.process_time()

with open('input.txt') as f:
    passcode = f.readlines()[0].strip()

moves = deque()
goal = (3, 3)
start = (0, 0)
node = (start, passcode)
moves.extend(explore_node(node))

while len(moves) > 0:
    m = moves.popleft()
    xy = m[0]
    if xy == goal:
        print('Problem 1:', m[1][len(passcode):])
        t = time.process_time() - t
        print('Time elapsed: {0} µs'.format(int(t * 1000000)))
        t = time.process_time()
        break
    moves.extend(explore_node(m))

moves.clear()
moves.extend(explore_node(node))
p2 = 0
found = 0

while len(moves) > 0 and found < 5000:
    m = moves.pop()
    xy = m[0]
    if xy == goal:
        p2 = max(p2, len(m[1]) - len(passcode))
        found += 1
        continue
    moves.extend(explore_node(m))
    
print('Problem 2:', p2)
t = time.process_time() - t
print('Time elapsed: {0} ms'.format(int(t * 1000)))
