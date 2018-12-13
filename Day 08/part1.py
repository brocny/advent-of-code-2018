import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
from input_loader import get_input
from collections import deque

def sumtree(t):
    ch = t.pop(0)
    md = t.pop(0)
    return sum(sumtree(t) for _ in range(ch)) + sum(t.pop(0) for _ in range(md))

def val(t):
    ch = t.pop(0)
    md = t.pop(0)
    vals = [val(t) for _ in range(ch)]
    mdata = [t.pop(0) for _ in range(md)]
    if ch == 0:
        return sum(mdata)
    return sum(vals[i-1] for i in mdata if i-1 in range(ch))

def solve(inp):
    t = [int(x) for x in inp.split()]
    part1 = sumtree(t)
    t = [int(x) for x in inp.split()]
    part2 = val(t)
    return part1, part2

print(solve(get_input(8)))