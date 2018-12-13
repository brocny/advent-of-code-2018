sum = 0
for x in open('input.txt').read().splitlines():
    num = int(x)
    sum += num

print(sum)


