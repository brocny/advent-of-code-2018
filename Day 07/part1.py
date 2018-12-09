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

for k in edges:
    edges[k] = sorted(edges[k])

S = [x for x in edges if in_degree[x] == 0]

while S:
    S.sort(reverse = True)
    n = S.pop()
    L.append(n)
    while edges[n]:
        m = edges[n].pop()
        in_degree[m] -= 1
        if in_degree[m] == 0:
            S.append(m)

workers = np.zeros(5)

for x in L:
    duration = 61 + ord(x) - ord('A')
    worker = workers.argmin()
    workers[worker] += duration

print(workers.max())
    

