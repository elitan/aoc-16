import time
import numpy as np

t = time.process_time()

def light(grid, cols, rows):
    grid[0:rows, 0:cols] = 1
    return grid
def rotate_col(grid, col_idx, offset):
    grid[:, col_idx] = np.roll(grid[:, col_idx], offset)
    return grid
def rotate_row(grid, row_idx, offset):
    grid[row_idx, :] = np.roll(grid[row_idx, :], offset)
    return grid

functions = {'rect': light, 'rotate column x': rotate_col,
             'rotate row y': rotate_row}

grid = np.empty((6, 50), dtype = np.int16)
grid[:] = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    line.strip()
    if line.startswith('rect'):
        args = line.split()
        cols, rows = map(int, args[1].split('x'))
        grid = functions[args[0]](grid, cols, rows)
    else:
        args = line.split('=')
        idx, offset = map(int, args[1].split(' by '))
        grid = functions[args[0]](grid, idx, offset)

print('Problem 1: {0}'.format(np.sum(grid)))
print('Problem 2:')
screen = []
for line in range(grid.shape[0]):
    s = ''
    for i, bit in enumerate(grid[line, :]):
        if bit == 1:
            s += '*'
        else:
            s += ' '
    screen.append(s)
    print(s)



t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 10000000)))

