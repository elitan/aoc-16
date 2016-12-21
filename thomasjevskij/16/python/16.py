import time

def mutate(a):
    s = a[::-1]
    b = ''
    for c in s:
        if c == '1':
            b += '0'
        else:
            b += '1'
    return a + '0' + b

def checksum(a):
    s = ''
    for i in range(0, len(a), 2):
        if a[i] == a[i + 1]:
            s += '1'
        else:
            s += '0'
    return s

def solve(a, length):
    while len(a) < length:
        a = mutate(a)
    a = a[:length]

    a = checksum(a)
    while len(a) % 2 == 0:
        a = checksum(a)
    return a

t = time.process_time()

with open('input.txt') as f:
    inp = f.readlines()[0].strip()
length = 272
    
print('Problem 1:', solve(inp, length))
t = time.process_time() - t
print('Elapsed time: {0} µs'.format(int(t * 10000000)))
t = time.process_time()

length = 35651584

print('Problem 2:', solve(inp, length))
t = time.process_time() - t
print('Elapsed time: {0} s'.format(t))
