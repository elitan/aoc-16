import time
import re
from collections import defaultdict, deque
from itertools import combinations
from random import choice
from copy import deepcopy

def move(state, indices, direction):
    components = list(*state[:-2])
    distance = state[-1] + 1
    new_floor = state[-2] + direction
    for i in indices:
        if i == -1:
            continue
        pair = list(components[i // 2])
        pair[i % 2] = new_floor
        components[i // 2] = tuple(pair)
        
    return (tuple(sorted(components, key=lambda x: 10*x[0]+x[1])), new_floor, distance)

def is_legal(state):
    components = state[0]
    for i, c in enumerate(components):
        rest = components[:i]+components[i+1:]
        if c[0] != c[1]:
            for r in rest:
                if c[0] == r[1]:
                    return False
    return True

def explore_node(state, visited):
    possible_nodes = []
    allowed = []
    for ii in range(2 * len(state[0])):
        c = state[0][ii // 2]
        if c[ii % 2] == state[-2]:
            allowed.append(ii)

    temp = []
    if state[-2] < 3:
        for double in combinations(allowed, 2):    
            new_node = move(state, double, 1)
            if is_legal(new_node) and new_node[:-1] not in visited:
                temp.append(new_node)
                visited.append(new_node[:-1])
        possible_nodes.extend(temp)
        if len(temp) == 0:
            temp.clear()
            for single in combinations(allowed, 1):
                    new_node = move(state, (single[0], -1), 1)
                    if is_legal(new_node) and new_node[:-1] not in visited:
                        temp.append(new_node)
                        visited.append(new_node[:-1])
            possible_nodes.extend(temp)
        temp.clear()
    if state[-2] > 0:
        for single in combinations(allowed, 1):
            new_node = move(state, (single[0], -1), -1)
            if is_legal(new_node) and new_node[:-1] not in visited:
                temp.append(new_node)
                visited.append(new_node[:-1])
        possible_nodes.extend(temp)
        
        if len(temp) == 0:
            temp.clear()
            for double in combinations(allowed, 2):
                new_node = move(state, double, -1)
                if is_legal(new_node) and new_node[:-1] not in visited:
                    temp.append(new_node)
                    visited.append(new_node[:-1])
            possible_nodes.extend(temp)
        temp.clear()
    return possible_nodes

def solve(start_state):
    visited = []
    visited.append(current_state[:-1])
    moves = deque()
    moves.extend(explore_node(current_state, visited))

    while len(moves) > 0:
        new_state = moves.popleft()
        if sum(sum(p) for p in new_state[0]) == len(new_state[0]) * 6:
            return new_state[-1]
            break
        
        moves.extend(explore_node(new_state, visited))

t = time.process_time()
with open('input.txt') as f:
    lines = f.readlines()

parsed_pairs = defaultdict(list)
pairs = []

for i, line in enumerate(lines):
    for microchip in re.findall(r'([a-z]+)-compatible', line):
        parsed_pairs[microchip].append(i)
for i, line in enumerate(lines):
    for generator in re.findall(r'([a-z]+) generator', line):
        parsed_pairs[generator].append(i)
for val in parsed_pairs.values():
    pairs.append(tuple(val))
# Encoding: [0] (pair, pair, ..., pair), [1]/[-2] Floor number [2]/[-1] Distance
current_state = (tuple(sorted(pairs, key=lambda x: 10*x[0]+x[1])), 0, 0)

print('Problem 1: {0}'.format(solve(current_state)))
t = time.process_time() - t
print("Time elapsed: {0} ms".format(int(t * 1000)))
t = time.process_time()

pairs.extend([(0, 0), (0, 0)])
current_state = (tuple(sorted(pairs, key=lambda x: 10*x[0]+x[1])), 0, 0)
print('Problem 2: {0}'.format(solve(current_state)))
t = time.process_time() - t
print("Time elapsed: {0} ms".format(int(t * 1000)))
