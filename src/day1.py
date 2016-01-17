position = 0
position_semaphore = 1
floor = 0

with open('../input/day1') as f:
    for line in f:
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            if position_semaphore:
                position += 1
                if floor == -1:
                    print('Santa entered the basement for the first time at position: ' + str(position))
                    position_semaphore = 0

print('Santa ends up at floor: ' + str(floor))
