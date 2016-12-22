import time
from math import log, floor, ceil
from collections import deque

t = time.process_time()

with open('input.txt') as f:
    num = int(f.readlines()[0].strip())

print('Problem 1:', 2 * (num - 2**floor(log(num, 2))) + 1)

t = time.process_time() - t
print('Time elapsed: {0} ms'.format(int(t * 1000)))
t = time.process_time()

print('Problem 2:', num - 3**floor(log(num, 3)))
print('Time elapsed: {0} ms'.format(int(t * 1000)))





