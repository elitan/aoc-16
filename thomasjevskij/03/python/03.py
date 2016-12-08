import time

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

count = 0
a_sides = []
b_sides = []
c_sides = []
for line in lines:
    triangle = list(map(int, line.strip().split()))
    a, b, c = sorted(triangle)
    count += int(a + b > c)
    a_sides.append(triangle[0])
    b_sides.append(triangle[1])
    c_sides.append(triangle[2])
    
print('Problem 1: {0:d}'.format(count))

count = 0
for ii in range(0, len(a_sides), 3):
    a, b, c = sorted(a_sides[ii:ii+3])
    count += int(a + b > c)

    a, b, c = sorted(b_sides[ii:ii+3])
    count += int(a + b > c)

    a, b, c = sorted(c_sides[ii:ii+3])
    count += int(a + b > c)


print('Problem 2: {0:d}'.format(count))
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 10000000)))
