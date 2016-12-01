import numpy as np
from numpy.linalg import norm
import time

t = time.process_time()

with open('input.txt') as f:
    instructions = f.readline().split(', ')
    
rotations = { 'L': np.mat('0, -1; 1, 0'), 'R': np.mat('0, 1; -1, 0') }
direction = np.array([0, 1])
direction.shape = (2, 1)
position = np.array([0, 0])
position.shape = (2, 1)    

for instruction in instructions:
    direction = np.matmul(rotations[instruction[0]], direction)
    position += int(instruction[1:]) * direction

print("Problem 1: %d"%int(norm(position, ord = 1)))
t = time.process_time() - t
print("Time elapsed: %d µs"%int(t * 10000000))
t = time.process_time()

position = np.array([0, 0])
position.shape = (2, 1) 

positions = set()
positions.add((position[0, 0], position[1, 0]))
done = False

for instruction in instructions:
    direction = np.matmul(rotations[instruction[0]], direction)
    for i in range(int(instruction[1:])):
        position += direction
        p = (position[0, 0], position[1, 0])
        if p in positions:
            done = True
            print('Problem 2: %d'%int(norm(position, ord = 1)))
            break
        else:
            positions.add(p)
    if done:
        break
    
t = time.process_time() - t
print("Time elapsed: %d µs"%int(t * 1000000))
