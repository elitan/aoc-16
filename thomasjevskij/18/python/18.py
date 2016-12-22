import time

def next_row(row):
    row = '.'+row+'.'
    new_row = ''
    not_allowed = ('^^.', '.^^', '^..', '..^')
    for i in range(1, len(row) - 1):
        seg = row[i-1:i+2]
        if seg in not_allowed:
            new_row += '^'
        else:
            new_row += '.'
    return new_row

t = time.process_time()

line = '.^^.^.^^^^'
with open('input.txt') as f:
    line = f.readlines()[0].strip()
p1 = line.count('.')

for i in range(39):
    line = next_row(line)
    p1 += line.count('.')
print('Problem 1:', p1)
t = time.process_time() - t
print('Time elapsed: {0} µs'.format(int(t * 1000000)))
t = time.process_time()

for i in range(400000 - 40):
    line = next_row(line)
    p1 += line.count('.')
print('Problem 2:', p1)
t = time.process_time() - t
print('Time elapsed: {0} s'.format(t))
