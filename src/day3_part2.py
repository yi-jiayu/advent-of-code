def drop_present():
    global houses, santa_x, santa_y, robosanta_x, robosanta_y, santas_turn
    if santas_turn:
        key = str(santa_x) + ', ' + str(santa_y)
    else:
        key = str(robosanta_x) + ', ' + str(robosanta_y)
    if key in houses:
        houses[key] += 1
    else:
        houses[key] = 1
    santas_turn = not santas_turn


def move(x, y):
    global santa_x, santa_y, robosanta_x, robosanta_y
    if santas_turn:
        santa_x += x
        santa_y += y
    else:
        robosanta_x += x
        robosanta_y += y

santa_x, santa_y = 0, 0
robosanta_x, robosanta_y = 0, 0
houses = dict()
santas_turn = True
houses['0, 0'] = 2

with open('../input/day3') as f:
    for line in f:
        for char in line:
            if char == '<':
                move(-1, 0)
            elif char == '>':
                move(1, 0)
            elif char == '^':
                move(0, 1)
            elif char == 'v':
                move(0, -1)
            drop_present()

print('Number of houses which receive more than one present: ' + str(len([house for house in houses.values() if house > 0])))
