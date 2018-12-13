import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
from input_loader import get_input
from collections import defaultdict
import numpy as np

lines = get_input(7).splitlines()


edges = defaultdict(list)
in_degree = defaultdict(int)
L = []


for line in lines:
    tokens = line.split()
    start, end = tokens[1], tokens[7]

    in_degree[end] += 1
    edges[start].append(end)


workers = [('%', 0) for i in range(5)]
time = 0

All = [x for x in edges]
All.append('U')
S = [x for x in All if in_degree[x] == 0]
T = 0

while All:
    for i in range(5):
        workers[i] = workers[i][0], max(workers[i][1] - T, 0)
    
    free_workers = [i for i in range(5) if workers[i][1] == 0]
    for j in free_workers:
        w = workers[j]
        if w[0] != '%':
            for x in edges[w[0]]:
                in_degree[x] -= 1
            workers[j] = '%', 0

    S = [x for x in All if in_degree[x] == 0]
    S.sort(reverse=True)
    for w in free_workers:
        if S:
            job = S.pop()
            All.remove(job)
            t = 61 + ord(job) - ord('A')
            workers[w] = (job, t)
            print(f'Staring {job} at {time}')
        else:
            break
    
    elapsed_time = min(filter(lambda w: w[0] != '%', workers), key=lambda w: w[1])[1]
    time += elapsed_time
    T = elapsed_time

print(time)
print(workers)
