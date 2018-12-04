import numpy as np

arr = np.ndarray((1000,1000), dtype='int')
dic = {}
count = 0
with open('input.txt') as f:
    for line in f:
        tokens = line.strip().split(' ')
        id = int(tokens[0][1:])
        coords = tokens[2].replace(':','').split(',')
        left, top = int(coords[0]), int(coords[1])
        size = tokens[3].split('x')
        width, height = int(size[0]), int(size[1])
        overlaps = False
        for x in range(left, left + width):
            for y in range(top, top + height):
                if arr[x,y] > 0:
                    overlaps = True
                    dic[arr[x,y]] = False

                arr[x,y] = id
        if not overlaps:
            dic[id] = True

print(list(filter(lambda x: x[1], dic.items())))
