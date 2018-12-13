import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
import numpy as np 

grid_serial = 2866
grid_size = 300
power = np.zeros([grid_size, grid_size])
for x in range(grid_size):
    for y in range(grid_size):
        p = (x + 10) * y + grid_serial
        p *= x + 10
        p = (p // 100) % 10
        power[x, y] = p - 5 

val_max = 0
arg_max = (0, 0, 0)
for step in range(1, grid_size - 2):
    print(f'Step: {step}')
    cells = np.zeros([grid_size - step + 1, grid_size - step + 1])
    for x in range(grid_size - step + 1):
        cells[x, 0] = sum(sum(power[x:x+step, :step]))
        for y in range(1, grid_size - step + 1):
            cells[x, y] = cells[x, y - 1] + sum(power[x:x + step, y +  step - 1]) - sum(power[x:x + step, y - 1])
            if cells[x, y] > val_max:
                val_max = cells[x, y]
                arg_max = (x, y, step)

print(arg_max)




        