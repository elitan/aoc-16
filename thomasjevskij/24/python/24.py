import time
from collections import deque
from itertools import permutations

def explore_node(rows, node, visited):
    added = []
    rowcol, distance = node
    row, col = rowcol
    
    directions = []
    if row > 0:
        directions.append((-1, 0))
    if row < len(rows) - 1:
        directions.append((1, 0))
    if col > 0:
        directions.append((0, -1))
    if col < len(rows[0]) - 1:
        directions.append((0, 1))
        
    for d in directions:
        new_row, new_col = row+d[0], col+d[1]
        
        if rows[new_row][new_col] != '#' and (new_row, new_col) not in visited:
            visited.append((new_row, new_col))
            added.append(((new_row, new_col), distance + 1))
    return added

t = time.process_time()

with open('input.txt') as f:
    rows = f.readlines()

locs = {}
for row in range(len(rows)):
    for col in range(len(rows[row])):
        if rows[row][col].isdigit():
            locs[rows[row][col]] = (row, col)

edges = {}
for j in range(int(max(locs.keys()))):
    for i in range(j, int(max(locs.keys())) + 1):
        visited = []
        moves = deque()
        visited.append(locs['{0}'.format(j)])
        goal = locs['{0}'.format(i)]
        start = (locs['{0}'.format(j)], 0)
        moves.extend(explore_node(rows, start, visited))

        while len(moves) > 0:
            m = moves.popleft()
            pos = m[0]
            if pos == goal:
                edges['{0}{1}'.format(j, i)] = edges['{0}{1}'.format(i, j)] = m[1]
                break
            moves.extend(explore_node(rows, m, visited))

p1 = 2**32
p2 = 2**32
for c in permutations('1234567'):
    path = '0'+''.join(c)
    p1 = min(sum(edges[path[i:i+2]] for i in range(len(path)-1)), p1)
    path += '0'
    p2 = min(sum(edges[path[i:i+2]] for i in range(len(path)-1)), p2)

print('Problem 1:', p1)
print('Problem 1:', p2)
t = time.process_time() - t
print("Time elapsed: {0} s".format(t))

