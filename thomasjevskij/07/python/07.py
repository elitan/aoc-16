import re
import time

t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

ABBA = 0
SSL = 0
for line in lines:
    support_ABBA = False
    support_SSL = False
    insides = re.findall(r'\[([a-z]+)\]', line)
    
    for rep in re.findall(r'(.)(\1{3,})', line):
        line = line.replace(rep[0]+rep[1], rep[0]+'--'+rep[0])
        
    if len(re.findall(r'([a-z])([a-z])\2\1', line)) > 0:
        support_ABBA = True        

    for k in insides:
        if len(re.findall(r'([a-z])([a-z])\2\1', k)) > 0:
            support_ABBA = False
            break

    for k in insides:
        line = line.replace('[' + k + ']', '---')

    for g in re.findall(r'(?=([a-z])([a-z])\1)', line):
        if g[0] == g[1]:
            continue
        bab = g[1]+g[0]+g[1]
        for k in insides:
            if bab in k:
                support_SSL = True
                break
            
    ABBA += int(support_ABBA)
    SSL += int(support_SSL)
print('Problem 1: {0}'.format(ABBA))
print('Problem 2: {0}'.format(SSL))
t = time.process_time() - t
print("Time elapsed: {0:d} ms".format(int(t * 1000)))

