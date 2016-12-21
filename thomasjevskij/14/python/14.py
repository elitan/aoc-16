import hashlib, time, re

t = time.process_time()

new_keys = []
stretched_keys = []

with open('input.txt') as f:
    salt = f.readlines()[0].strip()

hashes = []
stretched_hashes = []
triples = []
stretched_triples = []

for i in range(30000):
    k = '{0}{1}'.format(salt, i)
    m = hashlib.md5()
    m.update(k.encode('utf-8'))
    s = m.hexdigest()
    hashes.append(s)
    f = re.findall(r'(.)\1\1', s)
    if len(f) > 0:
        triples.append((i, f[0]))
    for j in range(2016):
        k = s
        m = hashlib.md5()
        m.update(k.encode('utf-8'))
        s = m.hexdigest()
    stretched_hashes.append(s)
    f = re.findall(r'(.)\1\1', s)
    if len(f) > 0:
        stretched_triples.append((i, f[0]))
        
while len(new_keys) < 64 and len(triples) > 0:
    i, c = triples.pop(0)
    for j in range(i + 1, min(i + 1001, len(hashes))):
        if c * 5 in hashes[j]:
            new_keys.append(i)
            break
while len(stretched_keys) < 64 and len(stretched_triples) > 0:
    i, c = stretched_triples.pop(0)
    for j in range(i + 1, min(i + 1001, len(stretched_hashes))):
        if c * 5 in stretched_hashes[j]:
            stretched_keys.append(i)
            break
   
print('Problem 1:', sorted(new_keys)[63])
print('Problem 2:', sorted(stretched_keys)[63])
t = time.process_time() - t
print('Elapsed time: {0} s'.format(t))
