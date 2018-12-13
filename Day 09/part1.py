import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
from input_loader import get_input
from collections import defaultdict, deque

tokens = get_input(9).split(' ')
turn = 0
circle = deque([0])
current_marble = 0
scores = defaultdict(int)
players, marbles = int(tokens[0]), int(tokens[-2]) * 100
for m in range(1, marbles + 1):
    if m % 23 == 0:
        scores[turn] += m
        circle.rotate(7)
        scores[turn] += circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(m)

    turn = (turn + 1) % players
    if m % 5000 == 0:
        print(f'{m} of {marbles}')

print(max(scores.values()))
