import time
from collections import namedtuple, defaultdict
from functools import reduce
import operator
import re

t = time.process_time()

def add_value(my_bots, outputs, value, bot):
    my_bots[bot].values.append(value)
    if len(my_bots[bot].values) >= 2 and len(my_bots[bot].instructions) >= 2:
        carry_out(my_bots, outputs, bot)

def add_instructions(my_bots, outputs, instructions, bot):
    my_bots[bot].instructions.extend(instructions)
    if len(my_bots[bot].values) >= 2:
        carry_out(my_bots, outputs, bot)

def carry_out(my_bots, outputs, bot):
    if len(set(my_bots[bot].values) & set([61, 17])) == 2:
            print('Problem 1: {0}'.format(bot))
    values = sorted(my_bots[bot].values)
    for i, s in enumerate(my_bots[bot].instructions):
        args = s.split()
        if args[0] == 'bot':
            add_value(my_bots, outputs, values[i], int(args[1]))
        else:
            outputs[int(args[1])].append(values[i])

Bot = namedtuple('Bot', ['values', 'instructions'])
my_bots = defaultdict(lambda: Bot([], []))
outputs = defaultdict(list)

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    if line.startswith('value'):
        value, bot = map(int, re.findall(r'\d+', line))
        add_value(my_bots, outputs, value, bot)
        
    if line.startswith('bot'):
        args = re.findall(r'[a-z]+ \d+', line)
        bot = int(args[0].split()[1])
        add_instructions(my_bots, outputs, args[1:], bot)

print('Problem 2: {0}'.format(reduce(operator.mul, (outputs[i][0] for i in range(3)))))
t = time.process_time() - t
print("Time elapsed: {0:d} µs".format(int(t * 1000000)))

