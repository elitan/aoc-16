import time

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()
m = 2**32

p = 0
count = 0
done = False
while len(lines) > 0:
    line = min(lines, key=lambda x: int(x[:x.find('-')]))
    lines.remove(line)
    low, high = map(int, line.strip().split('-'))
    if low <= p:
        p = max(p, high + 1)
    else:
        if not done:
            print('Problem 1:', p)
            done = True
        count += low - p
        p = max(p, high + 1)

count += m - p

print('Problem 2:', count)
t = time.process_time() - t
print('Time elapsed: {0} ms'.format(int(t * 1000)))
