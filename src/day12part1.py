import re

with open('../input/day12.txt') as f:
    inp = f.read()

numbers = re.findall(r'(-?\d+)', inp)
print(sum(int(x) for x in numbers))
