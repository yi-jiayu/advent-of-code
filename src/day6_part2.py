import re
import sys
from tqdm import tqdm


def adjust_brightness(op, x, y):
    global lights
    key = '{}, {}'.format(x, y)
    if op == 'turn off':
        if lights[key]:
            lights[key] -= 1
    elif op == 'toggle':
        lights[key] += 2
    elif op == 'turn on':
        lights[key] += 1


print('Generating light grid... ', end='')
sys.stdout.flush()

lights = {}

for i in range(1000):
    for j in range(1000):
        key = '{}, {}'.format(i, j)
        lights[key] = 0

print('Done!')

regex = re.compile(
        '(?P<op>(?:turn off)|(?:toggle)|(?:turn on)) (?P<c1x>\d+),(?P<c1y>\d+) through (?P<c2x>\d+),(?P<c2y>\d+)')

print('Calculating total number of operations required... ', end='')
sys.stdout.flush()

total_operations = 0

with open('../input/day6') as f:
    for line in f:
        match = regex.match(line)
        op, c1x, c1y, c2x, c2y = match.groups()
        c1x, c1y, c2x, c2y = int(c1x), int(c1y), int(c2x), int(c2y)
        total_operations += (c2y - c1y + 1) * (c2x - c1x + 1)

print('Done!')

print('Following instructions...')

with open('../input/day6') as f:
    with tqdm(total=total_operations, leave=True) as pbar:
        for line in f:
            match = regex.match(line)
            op, c1x, c1y, c2x, c2y = match.groups()
            c1x, c1y, c2x, c2y = int(c1x), int(c1y), int(c2x), int(c2y)
            for i in range(c1y, c2y + 1):
                for j in range(c1x, c2x + 1):
                    adjust_brightness(op, i, j)
                    pbar.update(1)

print('Done!')

print('Calculating total brightness... ', end='')
sys.stdout.flush()

total_brightness = 0

for i in range(1000):
    for j in range(1000):
        key = '{}, {}'.format(i, j)
        total_brightness += lights[key]

print('Done!')

print('The total brightness of all lights combined is {}!'.format(total_brightness))
