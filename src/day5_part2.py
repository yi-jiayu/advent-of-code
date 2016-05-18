def consecutive_pair_check(name):
    for i in range(len(name)):
        if name.count(name[i:i + 2]) > 1:
            return True
    return False


def letter_between_check(name):
    for i in range(len(name) - 3):
        if name[i] == name[i + 2]:
            return True
    return False

nice_string_count = 0

with open('../input/day5') as f:
    for line in f:
        if consecutive_pair_check(line):
            if letter_between_check(line):
                nice_string_count += 1

print('{} strings are nice!'.format(nice_string_count))
