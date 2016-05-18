import itertools

TARGET_CAPACITY = 150

containers = []

with open('../input/day17.txt') as f:
    for line in f:
        containers.append(int(line))

# print(containers)

num_possible_combinations = 0
min_containers_required = 0

second_half = False
for i in range(1, len(containers) + 1):
    combs = itertools.combinations(containers, i)
    possible = False
    for comb in combs:
        if sum(comb) == TARGET_CAPACITY:
            if not second_half:
                min_containers_required = i
            second_half = True
            possible = True
            num_possible_combinations += 1
    if not possible and second_half:
        break

print('Part 1 answer: {}'.format(num_possible_combinations))

num_combinations = 0
for comb in itertools.combinations(containers, min_containers_required):
    if sum(comb) == TARGET_CAPACITY:
        num_combinations += 1

print('Part 2 answer: {}'.format(num_combinations))
