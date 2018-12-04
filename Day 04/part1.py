import numpy as np
from collections import defaultdict
from functools import total_ordering

def parse_time(line: str):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])

lines = open('in.txt').read().split('\n')
lines.sort()

C = defaultdict(int)
CM = defaultdict(int)
guard = None

for line in lines:
    time = parse_time(line)
    if 'begins shift' in line:
        guard = int(line.split()[3][1:])
        asleep = None
    if 'falls asleep' in line:
        asleep = time
    if 'wakes up' in line:
        wake = time
        for t in range(asleep, time):
            C[guard] += 1
            CM[(guard, t)] += 1

def argmax(d: dict):
    max = None
    arg_max = None
    for k, v in d.items():
        if max is None or v > max:
            arg_max = k
            max = v

    return arg_max


best_guard = argmax(C)
for k, v in CM.items():
    if k[0] == best_guard:
        print(k[1], v)


print(best_guard)

guard, minute = argmax(CM)
print(guard * minute)
