import re


class Sue:
    def __init__(self, number: int, properties: dict):
        self.number = number
        self.properties = properties

    def __str__(self):
        return 'Sue {}: {}'.format(self.number, self.properties)


sue_regex = re.compile(r'Sue (\d+)')
prop_regex = re.compile(r'(\w+): (\d+)')

wanted_sue = {}

with open('../input/day16tickertape.txt') as f:
    for line in f:
        group = prop_regex.match(line).groups()
        prop, val = group
        wanted_sue[prop] = int(val)

# print(wanted_sue)

sues = []

with open('../input/day16.txt') as f:
    for line in f:
        num = sue_regex.search(line).group(1)
        properties = prop_regex.findall(line)
        sues.append(Sue(int(num), {prop: int(value) for prop, value in properties}))

for sue in sues:
    match = True
    for prop, val in wanted_sue.items():
        if prop in sue.properties.keys():
            if val != sue.properties[prop]:
                match = False
                continue
    if match:
        print('Part 1 answer: {}'.format(sue.number))

# Part 2
# Cats and trees: greater than
# Pomeranians and goldfish: less than
for sue in sues:
    match = True
    for prop, val in wanted_sue.items():
        if prop in sue.properties.keys():
            if prop in ('cats', 'trees'):
                current_prop = sue.properties[prop]
                if val >= current_prop:
                    match = False
                    continue
            elif prop in ('pomeranians', 'goldfish'):
                if val <= sue.properties[prop]:
                    match = False
                    continue
            else:
                if val != sue.properties[prop]:
                    match = False
                    continue
    if match:
        print('Part 2 answer: {}'.format(sue.number))


