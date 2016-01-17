def drop_present():
    global x, y, houses
    key = str(x) + ', ' + str(y)

    if key in houses:
        houses[key] += 1
    else:
        houses[key] = 1

x, y = 0, 0
houses = dict()
houses['0, 0'] = 1

with open('../input/day3') as f:
    for line in f:
        for char in line:
            if char == '>':
                x += 1
            elif char == '<':
                x -= 1
            elif char == '^':
                y += 1
            elif char == 'v':
                y -= 1
            drop_present()

print('Number of houses which receive more than one present: ' + str(len([house for house in houses.values() if house > 0])))


