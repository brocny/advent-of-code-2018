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
arr = np.zeros([400, 400, 2], dtype='int')

expanded = True
x_max = 0
y_max = 0
frontier = deque()
size = defaultdict(int)
data = []

for i, line in enumerate(lines):
        coords = line.replace(' ', '').split(',')
        x, y = int(coords[0]), int(coords[1])
        data.append((x,y))
        frontier.append((x, y, i + 1, 0))
        if x > x_max: x_max = x
        if y > y_max: y_max = y

arr = arr[:x_max, :y_max]


while frontier:
    x, y, i, d = frontier.pop()
    if x >= x_max or x < 0 or y >= y_max or y < 0: 
        size[i] = -1
        continue
    if arr[x,y,0] == 0:
        arr[x,y] = [i, d]
        frontier.appendleft((x + 1, y, i, d + 1))
        frontier.appendleft((x - 1, y, i, d + 1))
        frontier.appendleft((x, y + 1, i, d + 1))
        frontier.appendleft((x, y - 1, i, d + 1))
    elif arr[x, y, 0] > 0 and arr[x,y, 0] != i:
        if arr[x, y, 1] == d:
            arr[x,y,0] = -1
        elif arr[x,y,1] > d:
            arr[x,y] = [i, d]

for x in range(x_max):
    for y in range(y_max):
        el = arr[x,y,0]
        if el != -1 and size[el] >= 0:
            size[el] += 1

print(max(size.values()))

res2 = sum(sum(abs(x - k) + abs(y - l)
    for k,l in data) < 10000 for x in range(x_max) for y in range(y_max))

print(res2)   
