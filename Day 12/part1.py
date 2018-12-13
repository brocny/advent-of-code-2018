import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
from input_loader import get_input

inp = get_input(12).splitlines()
ext = 3
offset = 0
state = ['.' for _ in range(ext)] + list(inp[0].split(' ')[2]) + ['.' for _ in range(ext)]
rules = []
f_h, l_h = 0,0

for x in inp[2:]:
    t = x.split(' => ')
    if t[1] == '#':
        rules.append((list(t[0]), t[1]))

for gen in range(1000):
    new_state = ['.' for _ in range(len(state) + 4)]

    for k in range(2, len(state) - 2):
        for r in rules:
            if state[k - 2: k + 3] == r[0]:
                new_state[k] = r[1]
    
    
    f_h, l_h = 0, 0
    for i in range(len(new_state)):
        if new_state[i] == '#' and f_h == 0: f_h = i
        if new_state[i] == '#': l_h = i

    offset += f_h - 3
    state = ['.' for _ in range(3)] + new_state[f_h: f_h + l_h + 2]
    s = sum([x + offset - 3 for x, k in enumerate(state) if k == '#'])
    print(f'Gen {gen + 1}: {s}')
    print(f'offset: {offset}')

    print(s)
