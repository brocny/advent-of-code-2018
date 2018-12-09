import sys
import os
sys.path.append(os.path.abspath('../input_loader/'))
from input_loader import get_input

inp = list(get_input(5))

for l in range(26):
    ch = chr(ord('a') + l)
    copy = [x for x in inp if x.lower() != ch]
    
    stack = []
    for c in copy:
        if stack and c.swapcase() == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    print(len(stack))



print(len(stack))
