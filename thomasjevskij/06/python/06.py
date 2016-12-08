import time
from collections import defaultdict, Counter

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

freqs = defaultdict(str)
message1 = ''
message2 = ''
for line in lines:
    for ii in range(len(line.strip())):
        freqs[ii] += line[ii]
for k in sorted(freqs.keys()):
    c = Counter(freqs[k])
    message1 += c.most_common()[0][0]
    message2 += c.most_common()[-1][0]
    

print('Problem 1: {0}'.format(message1))
print('Problem 2: {0}'.format(message2))
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 10000000)))
