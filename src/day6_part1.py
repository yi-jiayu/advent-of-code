import re

lights = [int('0' * 1000, 2) for i in range(1000)]

regex = re.compile(
        r'(?P<op>(?:turn off)|(?:toggle)|(?:turn on)) (?P<c1x>\d+),(?P<c1y>\d+) through (?P<c2x>\d+),(?P<c2y>\d+)')

with open('../input/day6') as f:
    for line in f:
        match = regex.match(line)
        op, c1x, c1y, c2x, c2y = match.groups()
        c1x, c1y, c2x, c2y = int(c1x), int(c1y), int(c2x), int(c2y)
        for i in range(c1y, c2y + 1):
            if op == 'turn off':
                lights[i] &= int('1' * c1x + '0' * (c2x - c1x + 1) + '1' * (1000 - c2x - 1), 2)
            elif op == 'toggle':
                lights[i] ^= int('0' * c1x + '1' * (c2x - c1x + 1) + '0' * (1000 - c2x - 1), 2)
            elif op == 'turn on':
                lights[i] |= int('0' * c1x + '1' * (c2x - c1x + 1) + '0' * (1000 - c2x - 1), 2)

lights_turned_on = 0

for row in lights:
    lights_turned_on += bin(row).count('1')

print('{} lights are lit!'.format(lights_turned_on))
