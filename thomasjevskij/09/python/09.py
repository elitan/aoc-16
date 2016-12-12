import time

class Segment:
    def __init__(self, s, multiplier):
        self.multiplier = multiplier
        self.sub_segments = []
        self.s = s
        while '(' in self.s:
            i = self.s.find('(')
            offset = self.s[i:].find(')')
            chars, reps = map(int, self.s[i + 1:i + offset].split('x'))
            segment = self.s[i + offset + 1:i+offset+1+chars]
            self.sub_segments.append(Segment(segment, reps))
            self.s = self.s[:i] + self.s[i + offset + chars + 1:]
    
    def length(self):
        l = sum(sub.length() for sub in self.sub_segments) + len(self.s)
        return l * self.multiplier
            
def process_line(line):
    i = 0
    s = ''
    while i < len(line):
        if line[i] == '(':
            offset = line[i:].find(')')
                
            chars, repetitions = map(int, line[i + 1:i + offset].split('x'))
            s += (line[i + offset + 1:i + offset + 1 + chars]) * repetitions
            i += offset + chars + 1
            continue
        else:
            s += line[i]
            i += 1
    return len(s)
       
t = time.process_time()

with open('input.txt') as f:
    lines = f.readlines()

line = lines[0]

print('Problem 1: {0}'.format(process_line(line)))
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 1000000)))
t = time.process_time()

l = 0
i = 0
segs = []

while i < len(line):
    if line[i] == '(':
        offset = line[i:].find(')')
        chars, reps = map(int, line[i + 1:i + offset].split('x'))
        segment = line[i + offset + 1:i+offset+1+chars]
        segs.append(Segment(segment, reps))
        i += offset + chars + 1
    else:
        l += 1
        i += 1

print('Problem 2: {0}'.format(l + sum(seg.length() for seg in segs)))
t = time.process_time() - t
print("Time elapsed: {0:d} ms".format(int(t * 1000)))

