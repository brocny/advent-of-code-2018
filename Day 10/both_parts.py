import sys
import os
sys.path.append(os.path.abspath('../input_loader'))
from input_loader import get_input
import numpy as np
import re
import matplotlib.pyplot as plt
import imageio as im

lines = get_input(10).splitlines()

pointsx, pointsy, velocities = [], [], []
for line in lines:
    tokens = re.split('[<,>]', line.replace(' ',''))
    xpos = int(tokens[1])
    ypos = int(tokens[2])
    xvel = int(tokens[4])
    yvel = int(tokens[5])
    pointsx.append(xpos)
    pointsy.append(ypos)

    velocities.append((xvel, yvel))

size = 250
steps = 0
while max(pointsx) > size or max(pointsy) > size or min(pointsx) < -size or min(pointsy) < -size:
    for index, vel in enumerate(velocities):
        pointsx[index] += vel[0] * 5
        pointsy[index] += vel[1] * 5
        
    steps += 5


while True:
    for index, vel in enumerate(velocities):
        pointsx[index] += vel[0]
        pointsy[index] += vel[1]
    
    steps += 1
    print(steps)
    
    field = np.zeros([size, size])
    for i in range(len(pointsx)):
        field[pointsy[i], pointsx[i]] = 1

    plt.imshow(field)
    plt.show()

text = input("hello")

