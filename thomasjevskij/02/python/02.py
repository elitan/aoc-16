import time

t = time.process_time()

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

row, col = 1, 1
p1 = ''

for line in lines:
    for character in line:
        if character == 'U':
            row -= 1
        if character == 'D':
            row += 1
        if character == 'R':
            col += 1
        if character == 'L':
            col -= 1
        row = sorted((0, row, 2))[1]
        col = sorted((0, col, 2))[1]
        #row = min(max(row, 0), 2)
        #col = min(max(col, 0), 2)
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
forbidden = set(((0, 0), (0, 1), (0, 3), (0, 4), (1, 0), (1, 4),
                (3, 0), (3, 4), (4, 0), (4, 1), (4, 3), (4, 4)))
for line in lines:
    for character in line:
        if character == 'U':
            if (row - 1, col) not in forbidden:
                row -= 1
        if character == 'D':
            if (row + 1, col) not in forbidden:
                row += 1
        if character == 'R':
            if (row, col + 1) not in forbidden:
                col += 1
        if character == 'L':
            if (row, col - 1) not in forbidden:
                col -= 1
        row = sorted((0, row, 4))[1]
        col = sorted((0, col, 4))[1]
    p2 += key_pad[row][col]
        
print("Problem 2: " + p2)
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 10000000)))
