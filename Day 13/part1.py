import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
from input_loader import get_input
from functools import total_ordering


def dir_to_delta(direction: int) -> complex:
    return {
        0: complex(0, -1),
        1: complex(+1 ,0),
        2: complex(0, +1),
        3: complex(-1, 0)
    }[direction]


@total_ordering
class Train(object):
    def __init__(self, pos: complex, direc: int):
        self.pos = pos
        self.direc = direc
        self.dir_change = -1

    def delta(self):
        return dir_to_delta(self.dir)

    def __eq__(self, value):
        return self.pos == value.pos

    def __gt__(self, value):
        if self.pos.real > value.pos.real: return True
        elif self.pos.real < value.pos.real: return False
        return self.pos.imag > value.pos.imag

    def __str__(self):
        return f'Train {{pos = {self.pos}, dir = {self.direc}, dir_change = {self.dir_change}}}'


def char_to_dir(ch):
    return {
        '^' : 0,
        '>' : 1,
        'v' : 2,
        '<' : 3
    }.get(ch, - 1)



inp = list(map(lambda s: list(s), get_input(13).splitlines()))
height = len(inp)
width = max(len(inp[i]) for i in range(height))

field = inp

trains = []
id_t = 0
for y in range(height):
    for x in range(width):
        d = field[y][x]
        if d == 'v' or d == '^' or d == '>' or d == '<':
            field[y][x] = '|'
            trains.append(Train(complex(x, y), char_to_dir(d)))

print(trains)