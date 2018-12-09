import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
from input_loader import get_input
from collections import deque

numbers = list(map(int, get_input(8).split(' ')))
headerinds = deque([0])

while headerinds:
    ind = headerinds.pop()
    headerinds.append(ind + numbers[ind + 1])

print(headerinds)