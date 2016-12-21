import re
from functools import reduce
from collections import defaultdict
import string
import time

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

p1 = 0
for line in lines:
    real = True
    ID = int(re.findall(r'\d+', line)[0])
    checksum = re.findall(r'\[(.+)\]', line)[0]

    name = re.findall(r'(.+)-\d', line)[0]
    contents = defaultdict(list)
    for c in set(name.replace('-', '')):
        contents[name.count(c)].append(c)
    for ii in contents.keys():
        contents[ii] = sorted(contents[ii])

    top_five = []
    indices = []
    for ii in sorted(contents.keys(), reverse = True)[0:5]:
        for c in contents[ii]:
            indices.append(name.find(c))
            top_five.append((ii, c))
            
            if len(top_five) >= 5:
                break
        if len(top_five) >= 5:
                break                    
        
    for item in top_five:
        if item[1] not in checksum:
            real = False
            break
    p1 += int(real) * ID


print('Problem 1: {0:d}'.format(p1))   
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 10000000)))
t = time.process_time()


for line in lines:
    real = True
    ID = int(re.findall(r'\d+', line)[0])
    checksum = re.findall(r'\[(.+)\]', line)[0]

    name = re.findall(r'(.+)-\d', line)[0]
    new_name = ''
    for ch in name:
        if ch.isalpha():
            new_name += chr((ord(ch.lower()) - 97 + ID) % 26 + 97)
        else:
            new_name += ' '
    if 'north' in new_name:
        print('Problem 2: {0:d}'.format(ID))   
        t = time.process_time() - t
        print("Time elapsed: {0:d} µs".format(int(t * 10000000)))
        break


