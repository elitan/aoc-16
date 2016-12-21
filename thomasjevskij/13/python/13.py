import time

def open_space(xy, fav):
    x, y = xy
    num = '{0:b}'.format(x*x + 3*x + 2*x*y + y + y*y + fav).count('1')
    return num % 2 == 0

def explore_node(node, visited):
    added = []
    xy, distance = node
    x, y = xy
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for d in directions:
        new_node = (x + d[0], y + d[1])
        if sum(abs(a) for a in new_node) > sum(new_node):
            continue
        if open_space(new_node, fav) and new_node not in visited:
            visited.append(new_node)
            added.append((new_node, distance + 1))
    return added

t = time.process_time()

fav = 10
with open('input.txt') as f:
    fav = int(f.readlines()[0].strip())

visited = []
moves = []
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
p2 = set()
goal = (31, 39)

start = (1, 1)
visited.append(start)
p2.add(start)

node = (start, 0)
moves.extend(explore_node(node, visited))

while len(moves) > 0:
    m = moves.pop(0)
    if m[1] <= 50:
        p2.add(m[0])
    xy = m[0]
    if xy == goal:
        print('Problem 1:', m[1])
        print('Problem 2:', len(p2))
        t = time.process_time() - t
        print('Time elapsed: {0} µs'.format(int(t * 1000000)))
        break
    moves.extend(explore_node(m, visited))
#print(sorted(visited, key=lambda x: 10000*x[0]+x[1]))

