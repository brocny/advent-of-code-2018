import sys
import os
sys.path.append(os.path.abspath('../input_loader/'))
from input_loader import get_input
from collections import defaultdict, deque
import numpy as np

def mark(arr, x, y, i):
    if arr[x, y] == 0:
        arr[x,y] = i
        return True
    elif arr[x,y] > 0 and arr[x,y] != i:
        arr[x,y] = -1
        return False

lines = get_input(6).splitlines()
arr = np.zeros([400, 400], dtype='int')

expanded = True
x_max = 0
y_max = 0
frontier = deque()
size = defaultdict(int)

for i, line in enumerate(lines):
        coords = line.replace(' ', '').split(',')
        x, y = int(coords[0]), int(coords[1])
        frontier.append((x, y, 0, 0))
        if x > x_max: x_max = x
        if y > y_max: y_max = y

arr = arr[:x_max + 1, :y_max + 1]


while frontier:
    x, y, dist, dr = frontier.pop()
    arr[x,y] += dist
    if arr[x,y] > 100000:
        continue
    if dr != 1 and x < x_max - 1:    
       frontier.appendleft((x + 1, y, dist + 1, 2))
    if dr != 2 and x > 0: 
       frontier.appendleft((x - 1, y, dist + 1, 1))
    if dr != 3 and y < y_max - 1:
       frontier.appendleft((x, y + 1, dist + 1, 4))
    if dr != 4 and y > 0:
        frontier.appendleft((x, y - 1, dist + 1, 3))

