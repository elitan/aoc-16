import time

t = time.process_time()

functions = { 'U': lambda row, col: (row - 1, col),
              'D': lambda row, col: (row + 1, col),
              'L': lambda row, col: (row, col - 1),
              'R': lambda row, col: (row, col + 1) }

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

row, col = 1, 1
p1 = ''

for line in lines:
    for character in line:
        row, col = functions[character](row, col)
        row = sorted((0, row, 2))[1]
        col = sorted((0, col, 2))[1]
    p1 += '{0:d}'.format(3 * row + col + 1)

print("Problem 1: " + p1)
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 10000000)))
t = time.process_time()

key_pad = [ ('0', '0', '1', '0', '0'), ('0', '2', '3', '4', '0'),
            ('5', '6', '7', '8', '9'), ('0', 'A', 'B', 'C', '0'),
            ('0', '0', 'D', '0', '0') ]
row, col = 2, 0
p2 = ''
for line in lines:
    for character in line:
        new_row, new_col = functions[character](row, col)
        if sum(map(abs, (2 - new_row, 2 - new_col))) < 3:
            row, col = new_row, new_col
    p2 += key_pad[row][col]
        
print("Problem 2: " + p2)
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 10000000)))
